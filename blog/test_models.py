"""Contains tests for the models defined for the blog app."""
from datetime import datetime, timedelta

from django.test import TestCase
from django.conf import settings
import pytz
from .models import Article

# Create your tests here.
class ArticleTestCase(TestCase):
    """Test portfolio for Article class."""

    # Instance fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time_zone = pytz.timezone(settings.TIME_ZONE)
        self.prefix = "Last updated about"

    def setUp(self):
        # Static fields for this class
        # ArticleTestCase.time_zone = pytz.timezone(settings.TIME_ZONE)
        # ArticleTestCase.prefix = "Last updated about"

        Article.objects.create(
            title="test",
            sub_title="test_sub",
            date_submitted=datetime.now(self.time_zone) - timedelta(days=11),
            date_published=datetime.now(self.time_zone) - timedelta(days=10),
            date_updated=None,
        )

    def test_last_updated_1year_ago(self):
        """Date test one year ago"""
        # Arrange
        item = Article.objects.get(title="test")
        item.date_updated = datetime.now(self.time_zone) - timedelta(days=365)

        # Act
        result = item.last_updated

        # Assert
        self.assertEqual(result, f"{self.prefix} 1 year(s) ago")

    def test_last_updated_2years_ago(self):
        """Date test two years ago"""
        # Arrange
        item = Article.objects.get(title="test")
        item.date_updated = datetime.now(self.time_zone) - timedelta(days=731)

        # Act
        result = item.last_updated

        # Assert
        self.assertEqual(result, f"{self.prefix} 2 year(s) ago")

    def test_last_updated_1month_ago(self):
        """Date test one month ago"""
        # Arrange
        item = Article.objects.get(title="test")
        item.date_updated = datetime.now(self.time_zone) - timedelta(days=30)

        # Act
        result = item.last_updated

        # Assert
        self.assertEqual(result, f"{self.prefix} 1 month(s) ago")

    def test_last_updated_2months_ago(self):
        """Date test two months ago"""
        # Arrange
        item = Article.objects.get(title="test")
        item.date_updated = datetime.now(self.time_zone) - timedelta(days=68)

        # Act
        result = item.last_updated

        # Assert
        self.assertEqual(result, f"{self.prefix} 2 month(s) ago")

    def test_last_updated_1day_ago(self):
        """Date test one day ago"""
        # Arrange
        item = Article.objects.get(title="test")
        item.date_updated = datetime.now(self.time_zone) - timedelta(days=1)

        # Act
        result = item.last_updated

        # Assert
        self.assertEqual(result, f"{self.prefix} 1 day(s) ago")

    def test_last_updated_20days_ago(self):
        """Date test twenty days ago"""
        # Arrange
        item = Article.objects.get(title="test")
        item.date_updated = datetime.now(self.time_zone) - timedelta(days=20)

        # Act
        result = item.last_updated

        # Assert
        self.assertEqual(result, f"{self.prefix} 20 day(s) ago")

    def test_last_updated_1hour_ago(self):
        """Date test one hour ago"""
        # Arrange
        item = Article.objects.get(title="test")
        item.date_updated = datetime.now(self.time_zone) - timedelta(seconds=3600)

        # Act
        result = item.last_updated

        # Assert
        self.assertEqual(result, f"{self.prefix} 1 hour(s) ago")

    def test_last_updated_2hours_ago(self):
        """Date test two hours ago"""
        # Arrange
        item = Article.objects.get(title="test")
        item.date_updated = datetime.now(self.time_zone) - timedelta(seconds=7900)

        # Act
        result = item.last_updated

        # Assert
        self.assertEqual(result, f"{self.prefix} 2 hour(s) ago")

    def test_last_updated_1minute_ago(self):
        """Date test one minute ago"""
        # Arrange
        item = Article.objects.get(title="test")
        item.date_updated = datetime.now(self.time_zone) - timedelta(seconds=60)

        # Act
        result = item.last_updated

        # Assert
        self.assertEqual(result, f"{self.prefix} 1 minute(s) ago")

    def test_last_updated_2minutes_ago(self):
        """Date test two minutes ago"""
        # Arrange
        item = Article.objects.get(title="test")
        item.date_updated = datetime.now(self.time_zone) - timedelta(seconds=125)

        # Act
        result = item.last_updated

        # Assert
        self.assertEqual(result, f"{self.prefix} 2 minute(s) ago")

    def test_last_updated_seconds_ago(self):
        """Date test less than one minute ago"""
        # Arrange
        item = Article.objects.get(title="test")
        item.date_updated = datetime.now(self.time_zone) - timedelta(seconds=5)

        # Act
        result = item.last_updated

        # Assert
        self.assertEqual(result, f"{self.prefix} less than a minute ago")
