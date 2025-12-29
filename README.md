# ASDF X Post Generator - Discord Bot

[![CI](https://github.com/Ragnar-no-sleep/Discord-bot-X/actions/workflows/ci.yml/badge.svg)](https://github.com/Ragnar-no-sleep/Discord-bot-X/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![discord.py](https://img.shields.io/badge/discord.py-2.4.0-blue.svg)](https://discordpy.readthedocs.io/)
[![Railway](https://img.shields.io/badge/Deploy-Railway-blueviolet.svg)](https://railway.app)
[![GitHub last commit](https://img.shields.io/github/last-commit/Ragnar-no-sleep/Discord-bot-X)](https://github.com/Ragnar-no-sleep/Discord-bot-X/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/Ragnar-no-sleep/Discord-bot-X)](https://github.com/Ragnar-no-sleep/Discord-bot-X/issues)

Discord bot to generate X (Twitter) posts for the ASDF ecosystem.

## Features

- **Weekly post generation** - Generate all posts for a week with a single command
- **Raid posts** - Multiple styles (Kovni, Jean Terre, comparison, etc.)
- **Thread generation** - Full threads for each product + ecosystem
- **Cult/Philosophy posts** - Community building content
- **FUD responses** - Ready-to-use responses for all FUD types
- **Reply templates** - Engagement replies for different situations
- **Milestone posts** - Weekly stats and social proof
- **Export to file** - Download posts as .txt files
- **Daily reminders** - Automatic schedule notifications

## Setup

### 1. Create Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to "Bot" section and click "Add Bot"
4. Copy the **Token** (you'll need this)
5. Enable these intents:
   - MESSAGE CONTENT INTENT
6. Go to OAuth2 > URL Generator:
   - Scopes: `bot`, `applications.commands`
   - Permissions: `Send Messages`, `Embed Links`, `Attach Files`, `Read Message History`
7. Copy the generated URL and open it to invite the bot to your server

### 2. Install Dependencies

```bash
cd discordX-bot
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy example env file
cp .env.example .env

# Edit .env with your values
# DISCORD_TOKEN=your_token_here
# GUILD_ID=your_server_id (optional, for faster sync)
# OUTPUT_CHANNEL_ID=channel_for_reminders (optional)
```

### 4. Run the Bot

```bash
python bot.py
```

## Commands

### Post Generation

| Command | Description |
|---------|-------------|
| `/week [number]` | Generate all posts for week N |
| `/raid [product] [style]` | Generate a raid post |
| `/thread [type]` | Generate a full thread |
| `/cult` | Generate a cult/philosophy post |
| `/fud [type]` | Generate a FUD response |
| `/fudall [type]` | Get all responses for a FUD type |
| `/reply [type]` | Generate an engagement reply |
| `/milestone [week]` | Generate a milestone post |

### Info & Export

| Command | Description |
|---------|-------------|
| `/templates` | Show all available templates |
| `/schedule` | Show weekly posting schedule |
| `/help_posts` | Show help message |
| `/export [type]` | Export posts to .txt file |

## Raid Styles

- `imagine` - Kovni style ("Imagine...")
- `what_do_you_think` - Kovni style ("what do you think about...")
- `fuck_x` - Jean Terre style ("fuck dexscreener...")
- `comparison` - Direct comparison ($300 vs $20)
- `provocation` - Provocative style
- `viral` - Meme/viral format

## Thread Types

- `holdex` - HolDEX product thread (10 tweets)
- `ignition` - Ignition product thread (10 tweets)
- `asdforecast` - ASDForecast product thread (10 tweets)
- `ecosystem` - Full ecosystem thread (11 tweets)
- `builder_story` - Builder narrative thread (10 tweets)

## FUD Response Types

- `scam` - "It's a scam" responses
- `dead_chart` - "Chart is dead" responses
- `no_users` - "No one uses this" responses
- `how_money` - "How do you make money" responses
- `just_memecoin` - "Just a memecoin" responses
- `why_not_dexscreener` - "Why not use DexScreener" responses
- `copy` - "It's just a copy" responses
- `universal` - Universal FUD responses
- `nuclear` - Intense FUD responses

## File Structure

```
discordX-bot/
├── bot.py              # Main Discord bot
├── generator.py        # Post generation logic
├── config.py           # Templates, products, settings
├── requirements.txt    # Python dependencies
├── .env.example        # Environment template
├── .env                # Your configuration (create this)
└── README.md           # This file
```

## Customization

### Adding New Templates

Edit `config.py`:

1. **New raid template**: Add to `RAID_TEMPLATES` dict
2. **New thread**: Add to `THREAD_TEMPLATES` dict
3. **New FUD response**: Add to `FUD_RESPONSES` dict
4. **New product**: Add to `PRODUCTS` dict

### Updating Stats

Edit `CURRENT_STATS` in `config.py` to update milestone posts:

```python
CURRENT_STATS = {
    "products_live": 5,
    "supply_burned_percent": "7%+",
    "holdex_listings": "500+ listings processed",
    # etc.
}
```

### Modifying Schedule

Edit `WEEKLY_SCHEDULE` in `config.py` to change posting times and content.

## Future Enhancements

- [ ] Auto-post to X via API
- [ ] Post analytics tracking
- [ ] A/B testing for post styles
- [ ] Multi-language support
- [ ] Custom template creation via Discord
- [ ] Post scheduling queue
- [ ] Performance metrics dashboard

## Support

For issues or feature requests, contact the ASDF team.

---

**this is fine 🔥**
