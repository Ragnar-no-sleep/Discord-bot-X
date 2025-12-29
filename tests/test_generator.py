"""Tests for the post generator module."""

import pytest
from generator import PostGenerator, quick_raid, quick_thread, quick_cult, quick_fud_response


class TestPostGenerator:
    """Test cases for PostGenerator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.generator = PostGenerator()

    def test_generator_initialization(self):
        """Test that generator initializes correctly."""
        assert self.generator is not None
        assert self.generator.products is not None
        assert self.generator.hashtags is not None

    def test_generate_raid_comparison(self):
        """Test raid generation with comparison template."""
        post = self.generator.generate_raid("comparison", "holdex")
        assert post is not None
        assert len(post) > 0
        assert "holdex" in post.lower() or "HolDEX" in post

    def test_generate_raid_imagine(self):
        """Test raid generation with imagine template."""
        post = self.generator.generate_raid("imagine", "holdex")
        assert post is not None
        assert "Imagine" in post or "imagine" in post

    def test_generate_thread(self):
        """Test thread generation."""
        tweets = self.generator.generate_thread("ecosystem")
        assert tweets is not None
        assert isinstance(tweets, list)
        assert len(tweets) > 0

    def test_generate_cult_post(self):
        """Test cult post generation."""
        post = self.generator.generate_cult_post()
        assert post is not None
        assert len(post) > 0

    def test_generate_fud_response(self):
        """Test FUD response generation."""
        response = self.generator.generate_fud_response("scam")
        assert response is not None
        assert len(response) > 0

    def test_generate_fud_response_universal(self):
        """Test universal FUD response."""
        response = self.generator.generate_fud_response("universal")
        assert response is not None

    def test_generate_reply(self):
        """Test reply generation."""
        reply = self.generator.generate_reply("ecosystem")
        assert reply is not None
        assert len(reply) > 0

    def test_generate_milestone(self):
        """Test milestone post generation."""
        post = self.generator.generate_milestone(1)
        assert post is not None
        assert "week" in post.lower()

    def test_generate_weekly_posts(self):
        """Test weekly posts generation."""
        posts = self.generator.generate_weekly_posts(1)
        assert posts is not None
        assert isinstance(posts, dict)
        assert len(posts) > 0

    def test_export_weekly_posts(self):
        """Test weekly posts export."""
        output = self.generator.export_weekly_posts(1)
        assert output is not None
        assert "WEEK 1" in output

    def test_export_fud_responses(self):
        """Test FUD responses export."""
        output = self.generator.export_fud_responses()
        assert output is not None
        assert "FUD" in output

    def test_export_reply_templates(self):
        """Test reply templates export."""
        output = self.generator.export_reply_templates()
        assert output is not None
        assert "REPLY" in output


class TestQuickFunctions:
    """Test cases for quick generation functions."""

    def test_quick_raid(self):
        """Test quick raid function."""
        post = quick_raid("holdex", "comparison")
        assert post is not None

    def test_quick_thread(self):
        """Test quick thread function."""
        tweets = quick_thread("ecosystem")
        assert tweets is not None
        assert isinstance(tweets, list)

    def test_quick_cult(self):
        """Test quick cult function."""
        post = quick_cult()
        assert post is not None

    def test_quick_fud_response(self):
        """Test quick FUD response function."""
        response = quick_fud_response("universal")
        assert response is not None


class TestEdgeCases:
    """Test edge cases and error handling."""

    def setup_method(self):
        """Set up test fixtures."""
        self.generator = PostGenerator()

    def test_invalid_raid_template(self):
        """Test raid with invalid template defaults gracefully."""
        post = self.generator.generate_raid("invalid_template", "holdex")
        assert post is not None  # Should default to comparison

    def test_invalid_product(self):
        """Test raid with invalid product defaults gracefully."""
        post = self.generator.generate_raid("comparison", "invalid_product")
        assert post is not None  # Should default to holdex

    def test_invalid_thread_type(self):
        """Test thread with invalid type defaults gracefully."""
        tweets = self.generator.generate_thread("invalid_type")
        assert tweets is not None  # Should default to ecosystem

    def test_invalid_fud_type(self):
        """Test FUD response with invalid type defaults gracefully."""
        response = self.generator.generate_fud_response("invalid_type")
        assert response is not None  # Should default to universal

    def test_invalid_reply_type(self):
        """Test reply with invalid type defaults gracefully."""
        reply = self.generator.generate_reply("invalid_type")
        assert reply is not None  # Should default to ecosystem
