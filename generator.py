"""
ASDF X Post Generator - Generation Logic
=========================================
Generates posts based on templates and configuration.
"""

import random
from typing import List, Dict, Optional
from dataclasses import dataclass

from config import (
    PRODUCTS, HASHTAGS, PostType, DayOfWeek,
    RAID_TEMPLATES, THREAD_TEMPLATES, CULT_TEMPLATES,
    FUD_RESPONSES, REPLY_TEMPLATES, ANNOUNCEMENT_TEMPLATES,
    VIRAL_TEMPLATES, WEEKLY_SCHEDULE, CURRENT_STATS,
    get_hashtags, Product
)

@dataclass
class GeneratedPost:
    """Represents a generated post."""
    content: str
    post_type: PostType
    day: DayOfWeek
    time: str
    product: Optional[str] = None
    template_used: Optional[str] = None
    is_thread: bool = False
    thread_tweets: Optional[List[str]] = None

class PostGenerator:
    """Generates X posts based on templates and configuration."""

    def __init__(self):
        self.products = PRODUCTS
        self.hashtags = HASHTAGS
        self.current_stats = CURRENT_STATS

    # =========================================================================
    # RAID GENERATION
    # =========================================================================

    def generate_raid(self, template_name: str, product_key: str = "holdex") -> str:
        """Generate a raid post."""
        product = self.products.get(product_key)
        if not product:
            product = self.products["holdex"]

        hashtags = get_hashtags(PostType.RAID, product_key, "dexscreener")

        if template_name == "imagine":
            return self._generate_imagine_raid(product, hashtags)
        elif template_name == "what_do_you_think":
            return self._generate_what_do_you_think(product_key, hashtags)
        elif template_name == "fuck_x":
            return self._generate_fuck_x(product_key, hashtags)
        elif template_name == "comparison":
            return self._generate_comparison(product, hashtags)
        elif template_name == "provocation":
            return self._generate_provocation(product_key, hashtags)
        elif template_name == "viral":
            return self._generate_viral(hashtags)
        else:
            return self._generate_comparison(product, hashtags)

    def _generate_imagine_raid(self, product: Product, hashtags: str) -> str:
        """Generate an 'Imagine' style raid."""
        template = RAID_TEMPLATES["imagine"]["template"]
        return template.format(
            competitor=product.competitor,
            competitor_price=product.competitor_price,
            price=product.price,
            url=product.url,
            hashtags=hashtags
        )

    def _generate_what_do_you_think(self, product_key: str, hashtags: str) -> str:
        """Generate a 'What do you think' style raid."""
        template_data = RAID_TEMPLATES["what_do_you_think"]
        product = self.products[product_key]

        problem = template_data["problems"].get(product_key, "extractive fees")
        solution = template_data["solutions"].get(product_key, "burn fees instead")

        return template_data["template"].format(
            problem=problem,
            product_name=product.name,
            solution=solution,
            url=product.url,
            hashtags=hashtags
        )

    def _generate_fuck_x(self, product_key: str, hashtags: str) -> str:
        """Generate a 'Fuck X' style raid (Jean Terre style)."""
        template_data = RAID_TEMPLATES["fuck_x"]
        product = self.products[product_key]

        target_data = template_data["targets"].get(
            product_key,
            ("extractors", "taking your money", "$20. burned.")
        )
        target, complaint, value_prop = target_data

        return template_data["template"].format(
            target=target,
            complaint=complaint,
            product_name=product.name.lower(),
            value_prop=value_prop,
            url=product.url,
            hashtags=hashtags
        )

    def _generate_comparison(self, product: Product, hashtags: str) -> str:
        """Generate a comparison raid."""
        template = RAID_TEMPLATES["comparison"]["template"]
        return template.format(
            competitor=product.competitor,
            competitor_price=product.competitor_price,
            product_lower=product.name.lower(),
            price=product.price,
            url=product.url,
            hashtags=hashtags
        )

    def _generate_provocation(self, product_key: str, hashtags: str) -> str:
        """Generate a provocation raid."""
        template_data = RAID_TEMPLATES["provocation"]
        product = self.products[product_key]
        action = template_data["actions"].get(product_key, "extracting fees")

        return template_data["template"].format(
            competitor=product.competitor,
            action=action,
            product_lower=product.name.lower(),
            price=product.price,
            url=product.url,
            hashtags=hashtags
        )

    def _generate_viral(self, hashtags: str) -> str:
        """Generate a viral/meme post."""
        template = random.choice(VIRAL_TEMPLATES)
        return template.format(hashtags=hashtags)

    # =========================================================================
    # THREAD GENERATION
    # =========================================================================

    def generate_thread(self, thread_type: str) -> List[str]:
        """Generate a thread (list of tweets)."""
        if thread_type not in THREAD_TEMPLATES:
            thread_type = "ecosystem"

        hashtags = get_hashtags(PostType.THREAD, topic="building")
        tweets = THREAD_TEMPLATES[thread_type].copy()

        # Format hashtags in first and last tweets
        formatted_tweets = []
        for i, tweet in enumerate(tweets):
            if "{hashtags}" in tweet:
                formatted_tweets.append(tweet.format(hashtags=hashtags))
            else:
                formatted_tweets.append(tweet)

        return formatted_tweets

    # =========================================================================
    # CULT/PHILOSOPHY GENERATION
    # =========================================================================

    def generate_cult_post(self) -> str:
        """Generate a cult/philosophy post."""
        hashtags = get_hashtags(PostType.CULT)
        template = random.choice(CULT_TEMPLATES)
        return template.format(hashtags=hashtags)

    # =========================================================================
    # FUD RESPONSE GENERATION
    # =========================================================================

    def generate_fud_response(self, fud_type: str = "universal") -> str:
        """Generate a FUD response."""
        if fud_type not in FUD_RESPONSES:
            fud_type = "universal"

        responses = FUD_RESPONSES[fud_type]
        return random.choice(responses)

    def get_all_fud_responses(self) -> Dict[str, List[str]]:
        """Get all FUD responses organized by type."""
        return FUD_RESPONSES.copy()

    # =========================================================================
    # REPLY/ENGAGEMENT GENERATION
    # =========================================================================

    def generate_reply(self, reply_type: str = "ecosystem") -> str:
        """Generate an engagement reply."""
        if reply_type not in REPLY_TEMPLATES:
            reply_type = "ecosystem"
        return REPLY_TEMPLATES[reply_type]

    def get_all_replies(self) -> Dict[str, str]:
        """Get all reply templates."""
        return REPLY_TEMPLATES.copy()

    # =========================================================================
    # ANNOUNCEMENT GENERATION
    # =========================================================================

    def generate_milestone(self, week_num: int = 1) -> str:
        """Generate a milestone post."""
        hashtags = get_hashtags(PostType.MILESTONE)

        return ANNOUNCEMENT_TEMPLATES["milestone"].format(
            week_num=week_num,
            holdex_stat=self.current_stats["holdex_listings"],
            ignition_stat=self.current_stats["ignition_airdrops"],
            forecast_stat=self.current_stats["forecast_status"],
            burn_stat=self.current_stats["burn_status"],
            hashtags=hashtags
        )

    # =========================================================================
    # WEEKLY GENERATION
    # =========================================================================

    def generate_weekly_posts(self, week_num: int = 1) -> Dict[str, List[GeneratedPost]]:
        """Generate all posts for a week."""
        weekly_posts = {}

        for day, schedule in WEEKLY_SCHEDULE.items():
            day_name = day.name.capitalize()
            weekly_posts[day_name] = []

            for post_config in schedule["posts"]:
                post = self._generate_scheduled_post(day, post_config, week_num)
                if post:
                    weekly_posts[day_name].append(post)

        return weekly_posts

    def _generate_scheduled_post(
        self,
        day: DayOfWeek,
        config: Dict,
        week_num: int
    ) -> Optional[GeneratedPost]:
        """Generate a single scheduled post."""
        post_type = config["type"]
        template = config.get("template")
        product = config.get("product")
        time = config["time"]

        if post_type == PostType.THREAD:
            tweets = self.generate_thread(template)
            return GeneratedPost(
                content="\n\n---\n\n".join(tweets),
                post_type=post_type,
                day=day,
                time=time,
                template_used=template,
                is_thread=True,
                thread_tweets=tweets
            )

        elif post_type == PostType.RAID:
            content = self.generate_raid(template, product or "holdex")
            return GeneratedPost(
                content=content,
                post_type=post_type,
                day=day,
                time=time,
                product=product,
                template_used=template
            )

        elif post_type == PostType.CULT:
            content = self.generate_cult_post()
            return GeneratedPost(
                content=content,
                post_type=post_type,
                day=day,
                time=time
            )

        elif post_type == PostType.MILESTONE:
            content = self.generate_milestone(week_num)
            return GeneratedPost(
                content=content,
                post_type=post_type,
                day=day,
                time=time
            )

        return None

    # =========================================================================
    # EXPORT METHODS
    # =========================================================================

    def export_weekly_posts(self, week_num: int = 1) -> str:
        """Export weekly posts to formatted string."""
        posts = self.generate_weekly_posts(week_num)
        output = []
        output.append("=" * 80)
        output.append(f"ASDF ECOSYSTEM - WEEK {week_num} POSTS")
        output.append("Ready to Copy-Paste")
        output.append("=" * 80)
        output.append("")

        for day_name, day_posts in posts.items():
            output.append("=" * 80)
            output.append(f"{day_name.upper()}")
            output.append("=" * 80)
            output.append("")

            for i, post in enumerate(day_posts, 1):
                output.append("-" * 40)
                post_label = f"POST {i} - {post.post_type.value.upper()} ({post.time})"
                if post.is_thread:
                    post_label += " - THREAD"
                output.append(post_label)
                output.append("-" * 40)
                output.append("")

                if post.is_thread and post.thread_tweets:
                    for j, tweet in enumerate(post.thread_tweets, 1):
                        output.append(f"[TWEET {j}/{len(post.thread_tweets)} - START]")
                        output.append(tweet)
                        output.append("[END]")
                        output.append("")
                else:
                    output.append("[START]")
                    output.append(post.content)
                    output.append("[END]")
                    output.append("")

        return "\n".join(output)

    def export_fud_responses(self) -> str:
        """Export all FUD responses to formatted string."""
        output = []
        output.append("=" * 80)
        output.append("ASDF - FUD RESPONSES")
        output.append("Ready to Copy-Paste")
        output.append("=" * 80)
        output.append("")

        for fud_type, responses in FUD_RESPONSES.items():
            output.append("-" * 40)
            output.append(f"FUD TYPE: {fud_type.upper().replace('_', ' ')}")
            output.append("-" * 40)
            output.append("")

            for i, response in enumerate(responses, 1):
                output.append(f"[RESPONSE {i} - START]")
                output.append(response)
                output.append("[END]")
                output.append("")

        return "\n".join(output)

    def export_reply_templates(self) -> str:
        """Export all reply templates to formatted string."""
        output = []
        output.append("=" * 80)
        output.append("ASDF - REPLY TEMPLATES")
        output.append("Ready to Copy-Paste")
        output.append("=" * 80)
        output.append("")

        for reply_type, template in REPLY_TEMPLATES.items():
            output.append("-" * 40)
            output.append(f"REPLY TYPE: {reply_type.upper().replace('_', ' ')}")
            output.append("-" * 40)
            output.append("")
            output.append("[START]")
            output.append(template)
            output.append("[END]")
            output.append("")

        return "\n".join(output)


# =============================================================================
# QUICK GENERATION FUNCTIONS
# =============================================================================

def quick_raid(product: str = "holdex", style: str = "comparison") -> str:
    """Quickly generate a raid post."""
    generator = PostGenerator()
    return generator.generate_raid(style, product)

def quick_thread(thread_type: str = "ecosystem") -> List[str]:
    """Quickly generate a thread."""
    generator = PostGenerator()
    return generator.generate_thread(thread_type)

def quick_cult() -> str:
    """Quickly generate a cult post."""
    generator = PostGenerator()
    return generator.generate_cult_post()

def quick_fud_response(fud_type: str = "universal") -> str:
    """Quickly generate a FUD response."""
    generator = PostGenerator()
    return generator.generate_fud_response(fud_type)

def quick_reply(reply_type: str = "ecosystem") -> str:
    """Quickly generate a reply."""
    generator = PostGenerator()
    return generator.generate_reply(reply_type)


# =============================================================================
# CLI TEST
# =============================================================================

if __name__ == "__main__":
    generator = PostGenerator()

    print("\n" + "=" * 60)
    print("TESTING POST GENERATOR")
    print("=" * 60)

    print("\n--- RAID (Comparison) ---")
    print(generator.generate_raid("comparison", "holdex"))

    print("\n--- RAID (What do you think) ---")
    print(generator.generate_raid("what_do_you_think", "ignition"))

    print("\n--- CULT POST ---")
    print(generator.generate_cult_post())

    print("\n--- FUD RESPONSE (Scam) ---")
    print(generator.generate_fud_response("scam"))

    print("\n--- MILESTONE ---")
    print(generator.generate_milestone(1))

    print("\n" + "=" * 60)
    print("GENERATOR TESTS COMPLETE")
    print("=" * 60)
