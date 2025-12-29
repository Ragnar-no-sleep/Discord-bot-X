"""
ASDF X Post Generator - Discord Bot
====================================
Discord bot to generate X posts for the ASDF ecosystem.

Commands:
- /week [number] - Generate all posts for a week
- /raid [product] [style] - Generate a raid post
- /thread [type] - Generate a thread
- /cult - Generate a cult/philosophy post
- /fud [type] - Generate a FUD response
- /reply [type] - Generate an engagement reply
- /milestone [week] - Generate a milestone post
- /templates - Show all available templates
- /help_posts - Show help for post generation
"""

import os
import discord
from discord import app_commands
from discord.ext import commands, tasks
from dotenv import load_dotenv
from datetime import datetime, time
import asyncio
from typing import List

from generator import PostGenerator
from config import (
    PRODUCTS, DayOfWeek, WEEKLY_SCHEDULE,
    THREAD_TEMPLATES, FUD_RESPONSES, REPLY_TEMPLATES,
    RAID_TEMPLATES
)

# Load environment variables
load_dotenv()

# Bot configuration
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')  # Optional: for faster command sync
OUTPUT_CHANNEL_ID = os.getenv('OUTPUT_CHANNEL_ID')  # Channel for scheduled posts

# Initialize bot
intents = discord.Intents.default()
# Note: message_content intent not needed for slash commands only
# If you want to use prefix commands, enable it in Discord Developer Portal

bot = commands.Bot(command_prefix='!', intents=intents)
generator = PostGenerator()

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def split_message(content: str, max_length: int = 1900) -> List[str]:
    """Split a long message into chunks."""
    if len(content) <= max_length:
        return [content]

    chunks = []
    lines = content.split('\n')
    current_chunk = ""

    for line in lines:
        if len(current_chunk) + len(line) + 1 > max_length:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = line
        else:
            current_chunk += ('\n' if current_chunk else '') + line

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def format_post_for_discord(content: str, title: str = None) -> str:
    """Format a post for Discord display."""
    output = ""
    if title:
        output += f"**{title}**\n\n"
    output += "```\n"
    output += content
    output += "\n```"
    return output

def create_embed(title: str, description: str, color: int = 0x00ff00) -> discord.Embed:
    """Create a Discord embed."""
    embed = discord.Embed(
        title=title,
        description=description,
        color=color,
        timestamp=datetime.utcnow()
    )
    embed.set_footer(text="ASDF X Post Generator")
    return embed

# =============================================================================
# BOT EVENTS
# =============================================================================

@bot.event
async def on_ready():
    """Called when bot is ready."""
    print(f'✅ {bot.user} is now running!')
    print(f'📊 Connected to {len(bot.guilds)} guild(s)')

    # Sync commands
    try:
        if GUILD_ID:
            guild = discord.Object(id=int(GUILD_ID))
            synced = await bot.tree.sync(guild=guild)
            print(f'🔄 Synced {len(synced)} command(s) to guild {GUILD_ID}')
        else:
            synced = await bot.tree.sync()
            print(f'🔄 Synced {len(synced)} command(s) globally')
    except Exception as e:
        print(f'❌ Failed to sync commands: {e}')

    # Start scheduled tasks if channel is configured (only if not already running)
    if OUTPUT_CHANNEL_ID and not daily_post_reminder.is_running():
        daily_post_reminder.start()
        print('⏰ Scheduled tasks started')

# =============================================================================
# SLASH COMMANDS
# =============================================================================

# -----------------------------------------------------------------------------
# /week - Generate weekly posts
# -----------------------------------------------------------------------------

@bot.tree.command(name="week", description="Generate all posts for a week")
@app_commands.describe(week_number="Week number (default: 1)")
async def week_command(interaction: discord.Interaction, week_number: int = 1):
    """Generate all posts for a week."""
    await interaction.response.defer()

    try:
        output = generator.export_weekly_posts(week_number)
        chunks = split_message(output, 1900)

        # Send first message as response
        await interaction.followup.send(f"**📅 WEEK {week_number} POSTS GENERATED**\n\n*Sending {len(chunks)} message(s)...*")

        # Send remaining chunks
        for i, chunk in enumerate(chunks):
            await interaction.channel.send(f"```\n{chunk}\n```")
            if i < len(chunks) - 1:
                await asyncio.sleep(0.5)  # Avoid rate limiting

    except Exception as e:
        await interaction.followup.send(f"❌ Error generating posts: {str(e)}")

# -----------------------------------------------------------------------------
# /raid - Generate raid post
# -----------------------------------------------------------------------------

@bot.tree.command(name="raid", description="Generate a raid post")
@app_commands.describe(
    product="Product to promote",
    style="Raid style"
)
@app_commands.choices(
    product=[
        app_commands.Choice(name="HolDEX", value="holdex"),
        app_commands.Choice(name="Ignition", value="ignition"),
        app_commands.Choice(name="ASDForecast", value="asdforecast"),
    ],
    style=[
        app_commands.Choice(name="Imagine (Kovni style)", value="imagine"),
        app_commands.Choice(name="What do you think (Kovni style)", value="what_do_you_think"),
        app_commands.Choice(name="Fuck X (Jean Terre style)", value="fuck_x"),
        app_commands.Choice(name="Comparison", value="comparison"),
        app_commands.Choice(name="Provocation", value="provocation"),
        app_commands.Choice(name="Viral/Meme", value="viral"),
    ]
)
async def raid_command(
    interaction: discord.Interaction,
    product: str = "holdex",
    style: str = "comparison"
):
    """Generate a raid post."""
    try:
        post = generator.generate_raid(style, product)

        embed = create_embed(
            f"🔥 RAID POST - {product.upper()}",
            f"Style: **{style.replace('_', ' ').title()}**",
            color=0xff5500
        )

        await interaction.response.send_message(embed=embed)
        await interaction.channel.send(format_post_for_discord(post, "📋 Copy this:"))

    except Exception as e:
        await interaction.response.send_message(f"❌ Error: {str(e)}")

# -----------------------------------------------------------------------------
# /thread - Generate thread
# -----------------------------------------------------------------------------

@bot.tree.command(name="thread", description="Generate a thread")
@app_commands.describe(thread_type="Type of thread")
@app_commands.choices(
    thread_type=[
        app_commands.Choice(name="HolDEX", value="holdex"),
        app_commands.Choice(name="Ignition", value="ignition"),
        app_commands.Choice(name="ASDForecast", value="asdforecast"),
        app_commands.Choice(name="Ecosystem", value="ecosystem"),
        app_commands.Choice(name="Builder Story", value="builder_story"),
    ]
)
async def thread_command(interaction: discord.Interaction, thread_type: str = "ecosystem"):
    """Generate a thread."""
    await interaction.response.defer()

    try:
        tweets = generator.generate_thread(thread_type)

        await interaction.followup.send(f"**🧵 THREAD GENERATED - {thread_type.upper()}**\n\n*{len(tweets)} tweets*")

        for i, tweet in enumerate(tweets, 1):
            header = f"**Tweet {i}/{len(tweets)}**"
            await interaction.channel.send(f"{header}\n```\n{tweet}\n```")
            await asyncio.sleep(0.3)

    except Exception as e:
        await interaction.followup.send(f"❌ Error: {str(e)}")

# -----------------------------------------------------------------------------
# /cult - Generate cult post
# -----------------------------------------------------------------------------

@bot.tree.command(name="cult", description="Generate a cult/philosophy post")
async def cult_command(interaction: discord.Interaction):
    """Generate a cult/philosophy post."""
    try:
        post = generator.generate_cult_post()

        embed = create_embed(
            "💊 CULT POST",
            "Philosophy & conviction content",
            color=0x9b59b6
        )

        await interaction.response.send_message(embed=embed)
        await interaction.channel.send(format_post_for_discord(post, "📋 Copy this:"))

    except Exception as e:
        await interaction.response.send_message(f"❌ Error: {str(e)}")

# -----------------------------------------------------------------------------
# /fud - Generate FUD response
# -----------------------------------------------------------------------------

@bot.tree.command(name="fud", description="Generate a FUD response")
@app_commands.describe(fud_type="Type of FUD to respond to")
@app_commands.choices(
    fud_type=[
        app_commands.Choice(name="Scam accusations", value="scam"),
        app_commands.Choice(name="Dead chart", value="dead_chart"),
        app_commands.Choice(name="No users", value="no_users"),
        app_commands.Choice(name="How do you make money", value="how_money"),
        app_commands.Choice(name="Just a memecoin", value="just_memecoin"),
        app_commands.Choice(name="Why not DexScreener", value="why_not_dexscreener"),
        app_commands.Choice(name="It's just a copy", value="copy"),
        app_commands.Choice(name="Universal response", value="universal"),
        app_commands.Choice(name="Nuclear response", value="nuclear"),
    ]
)
async def fud_command(interaction: discord.Interaction, fud_type: str = "universal"):
    """Generate a FUD response."""
    try:
        response = generator.generate_fud_response(fud_type)

        embed = create_embed(
            f"🛡️ FUD RESPONSE - {fud_type.upper().replace('_', ' ')}",
            "Ready to counter FUD",
            color=0xe74c3c
        )

        await interaction.response.send_message(embed=embed)
        await interaction.channel.send(format_post_for_discord(response, "📋 Copy this:"))

    except Exception as e:
        await interaction.response.send_message(f"❌ Error: {str(e)}")

# -----------------------------------------------------------------------------
# /fudall - Get all FUD responses
# -----------------------------------------------------------------------------

@bot.tree.command(name="fudall", description="Get all FUD responses for a type")
@app_commands.describe(fud_type="Type of FUD")
@app_commands.choices(
    fud_type=[
        app_commands.Choice(name="Scam accusations", value="scam"),
        app_commands.Choice(name="Dead chart", value="dead_chart"),
        app_commands.Choice(name="No users", value="no_users"),
        app_commands.Choice(name="How do you make money", value="how_money"),
        app_commands.Choice(name="Just a memecoin", value="just_memecoin"),
        app_commands.Choice(name="Why not DexScreener", value="why_not_dexscreener"),
        app_commands.Choice(name="It's just a copy", value="copy"),
        app_commands.Choice(name="Universal response", value="universal"),
        app_commands.Choice(name="Nuclear response", value="nuclear"),
    ]
)
async def fudall_command(interaction: discord.Interaction, fud_type: str = "universal"):
    """Get all FUD responses for a specific type."""
    await interaction.response.defer()

    try:
        responses = FUD_RESPONSES.get(fud_type, FUD_RESPONSES["universal"])

        await interaction.followup.send(f"**🛡️ ALL FUD RESPONSES - {fud_type.upper().replace('_', ' ')}**\n\n*{len(responses)} response(s)*")

        for i, response in enumerate(responses, 1):
            await interaction.channel.send(f"**Response {i}:**\n```\n{response}\n```")
            await asyncio.sleep(0.3)

    except Exception as e:
        await interaction.followup.send(f"❌ Error: {str(e)}")

# -----------------------------------------------------------------------------
# /reply - Generate engagement reply
# -----------------------------------------------------------------------------

@bot.tree.command(name="reply", description="Generate an engagement reply")
@app_commands.describe(reply_type="Type of reply")
@app_commands.choices(
    reply_type=[
        app_commands.Choice(name="Discovery - HolDEX", value="discovery_holdex"),
        app_commands.Choice(name="Discovery - Ignition", value="discovery_ignition"),
        app_commands.Choice(name="Ecosystem pitch", value="ecosystem"),
        app_commands.Choice(name="Challenge - HolDEX", value="challenge_holdex"),
        app_commands.Choice(name="Challenge - Ignition", value="challenge_ignition"),
        app_commands.Choice(name="High fees discussion", value="high_fees"),
        app_commands.Choice(name="Launchpad dump complaint", value="launchpad_dump"),
        app_commands.Choice(name="Solana projects question", value="solana_projects"),
        app_commands.Choice(name="Building discussion", value="building"),
    ]
)
async def reply_command(interaction: discord.Interaction, reply_type: str = "ecosystem"):
    """Generate an engagement reply."""
    try:
        reply = generator.generate_reply(reply_type)

        embed = create_embed(
            f"💬 REPLY TEMPLATE - {reply_type.upper().replace('_', ' ')}",
            "Engagement reply",
            color=0x3498db
        )

        await interaction.response.send_message(embed=embed)
        await interaction.channel.send(format_post_for_discord(reply, "📋 Copy this:"))

    except Exception as e:
        await interaction.response.send_message(f"❌ Error: {str(e)}")

# -----------------------------------------------------------------------------
# /milestone - Generate milestone post
# -----------------------------------------------------------------------------

@bot.tree.command(name="milestone", description="Generate a milestone post")
@app_commands.describe(week_number="Week number")
async def milestone_command(interaction: discord.Interaction, week_number: int = 1):
    """Generate a milestone post."""
    try:
        post = generator.generate_milestone(week_number)

        embed = create_embed(
            f"📊 MILESTONE POST - WEEK {week_number}",
            "Social proof content",
            color=0x2ecc71
        )

        await interaction.response.send_message(embed=embed)
        await interaction.channel.send(format_post_for_discord(post, "📋 Copy this:"))

    except Exception as e:
        await interaction.response.send_message(f"❌ Error: {str(e)}")

# -----------------------------------------------------------------------------
# /templates - Show available templates
# -----------------------------------------------------------------------------

@bot.tree.command(name="templates", description="Show all available templates")
async def templates_command(interaction: discord.Interaction):
    """Show all available templates."""
    embed = discord.Embed(
        title="📚 AVAILABLE TEMPLATES",
        color=0xf39c12,
        timestamp=datetime.utcnow()
    )

    # Raid styles
    raid_styles = list(RAID_TEMPLATES.keys())
    embed.add_field(
        name="🔥 Raid Styles",
        value="\n".join([f"• `{s}`" for s in raid_styles]),
        inline=True
    )

    # Thread types
    thread_types = list(THREAD_TEMPLATES.keys())
    embed.add_field(
        name="🧵 Thread Types",
        value="\n".join([f"• `{t}`" for t in thread_types]),
        inline=True
    )

    # FUD types
    fud_types = list(FUD_RESPONSES.keys())
    embed.add_field(
        name="🛡️ FUD Types",
        value="\n".join([f"• `{f}`" for f in fud_types]),
        inline=True
    )

    # Products
    products = list(PRODUCTS.keys())
    embed.add_field(
        name="📦 Products",
        value="\n".join([f"• `{p}`" for p in products]),
        inline=True
    )

    # Reply types
    reply_types = list(REPLY_TEMPLATES.keys())
    embed.add_field(
        name="💬 Reply Types",
        value="\n".join([f"• `{r}`" for r in reply_types[:5]]) + f"\n• *+{len(reply_types)-5} more*",
        inline=True
    )

    embed.set_footer(text="Use /help_posts for command usage")
    await interaction.response.send_message(embed=embed)

# -----------------------------------------------------------------------------
# /help_posts - Show help
# -----------------------------------------------------------------------------

@bot.tree.command(name="help_posts", description="Show help for post generation")
async def help_command(interaction: discord.Interaction):
    """Show help for post generation."""
    embed = discord.Embed(
        title="🤖 ASDF X POST GENERATOR - HELP",
        description="Generate X posts for the ASDF ecosystem",
        color=0x00ff00,
        timestamp=datetime.utcnow()
    )

    commands_info = """
**📅 Weekly Posts**
`/week [number]` - Generate all posts for a week

**🔥 Raids**
`/raid [product] [style]` - Generate a raid post

**🧵 Threads**
`/thread [type]` - Generate a thread

**💊 Cult**
`/cult` - Generate a cult/philosophy post

**🛡️ FUD Responses**
`/fud [type]` - Generate a single FUD response
`/fudall [type]` - Get all responses for a FUD type

**💬 Replies**
`/reply [type]` - Generate an engagement reply

**📊 Milestones**
`/milestone [week]` - Generate a milestone post

**📚 Info**
`/templates` - Show all available templates
`/help_posts` - Show this help message
"""

    embed.add_field(name="Commands", value=commands_info, inline=False)

    tips = """
• Posts are formatted for easy copy-paste
• Threads are split into individual tweets
• Use `/templates` to see all options
• Hashtags are automatically added
"""
    embed.add_field(name="💡 Tips", value=tips, inline=False)

    await interaction.response.send_message(embed=embed)

# -----------------------------------------------------------------------------
# /schedule - Show weekly schedule
# -----------------------------------------------------------------------------

@bot.tree.command(name="schedule", description="Show the weekly posting schedule")
async def schedule_command(interaction: discord.Interaction):
    """Show the weekly posting schedule."""
    embed = discord.Embed(
        title="📅 WEEKLY POSTING SCHEDULE",
        description="Recommended posting times (CET/Paris)",
        color=0x3498db,
        timestamp=datetime.utcnow()
    )

    for day, schedule in WEEKLY_SCHEDULE.items():
        day_name = day.name.capitalize()
        theme = schedule["theme"]
        posts_info = []

        for post in schedule["posts"]:
            post_type = post["type"].value
            time_str = post["time"]
            template = post.get("template", "random")
            posts_info.append(f"`{time_str}` - {post_type} ({template})")

        embed.add_field(
            name=f"**{day_name}** - {theme}",
            value="\n".join(posts_info) if posts_info else "No scheduled posts",
            inline=False
        )

    embed.set_footer(text="Times are in CET (Paris timezone)")
    await interaction.response.send_message(embed=embed)

# -----------------------------------------------------------------------------
# /export - Export posts to file
# -----------------------------------------------------------------------------

@bot.tree.command(name="export", description="Export posts to a text file")
@app_commands.describe(
    export_type="What to export",
    week_number="Week number (for weekly export)"
)
@app_commands.choices(
    export_type=[
        app_commands.Choice(name="Weekly posts", value="weekly"),
        app_commands.Choice(name="FUD responses", value="fud"),
        app_commands.Choice(name="Reply templates", value="replies"),
    ]
)
async def export_command(
    interaction: discord.Interaction,
    export_type: str = "weekly",
    week_number: int = 1
):
    """Export posts to a text file."""
    await interaction.response.defer()

    try:
        if export_type == "weekly":
            content = generator.export_weekly_posts(week_number)
            filename = f"week{week_number}_posts.txt"
        elif export_type == "fud":
            content = generator.export_fud_responses()
            filename = "fud_responses.txt"
        elif export_type == "replies":
            content = generator.export_reply_templates()
            filename = "reply_templates.txt"
        else:
            content = generator.export_weekly_posts(1)
            filename = "posts.txt"

        # Create file and send
        file = discord.File(
            fp=__import__('io').StringIO(content),
            filename=filename
        )

        await interaction.followup.send(
            f"📄 **Export complete!** Here's your `{filename}`:",
            file=file
        )

    except Exception as e:
        await interaction.followup.send(f"❌ Error exporting: {str(e)}")

# =============================================================================
# SCHEDULED TASKS
# =============================================================================

@tasks.loop(time=time(hour=8, minute=0))  # 8 AM daily
async def daily_post_reminder():
    """Send daily posting reminder."""
    if not OUTPUT_CHANNEL_ID:
        return

    channel = bot.get_channel(int(OUTPUT_CHANNEL_ID))
    if not channel:
        return

    # Get today's schedule
    today = DayOfWeek(datetime.now().weekday())
    schedule = WEEKLY_SCHEDULE.get(today)

    if not schedule:
        return

    embed = discord.Embed(
        title=f"📅 TODAY'S POSTING SCHEDULE - {today.name}",
        description=f"Theme: **{schedule['theme']}**",
        color=0x00ff00,
        timestamp=datetime.utcnow()
    )

    posts_info = []
    for post in schedule["posts"]:
        post_type = post["type"].value
        time_str = post["time"]
        template = post.get("template", "random")
        product = post.get("product", "")
        posts_info.append(f"⏰ `{time_str}` - **{post_type}** ({template}) {product}")

    embed.add_field(
        name="Posts for today:",
        value="\n".join(posts_info) if posts_info else "No posts scheduled",
        inline=False
    )

    embed.add_field(
        name="Quick commands:",
        value="Use `/week` to generate all posts\nUse `/raid`, `/thread`, `/cult` for individual posts",
        inline=False
    )

    await channel.send(embed=embed)

# =============================================================================
# ERROR HANDLING
# =============================================================================

@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    """Handle slash command errors."""
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message("❌ You don't have permission to use this command.", ephemeral=True)
    elif isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(f"⏳ Command on cooldown. Try again in {error.retry_after:.2f}s", ephemeral=True)
    else:
        await interaction.response.send_message(f"❌ An error occurred: {str(error)}", ephemeral=True)
        print(f"Command error: {error}")

# =============================================================================
# MAIN
# =============================================================================

def main():
    """Run the bot."""
    if not TOKEN:
        print("❌ DISCORD_TOKEN not found in environment variables!")
        print("Please create a .env file with your Discord bot token.")
        print("See .env.example for reference.")
        return

    print("🚀 Starting ASDF X Post Generator Bot...")
    bot.run(TOKEN)

if __name__ == "__main__":
    main()
