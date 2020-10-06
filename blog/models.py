"""Contains database models for the Blog App.
"""

from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
import pytz
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Article(models.Model):
    """Model definition for Article."""

    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250, blank=True)
    date_submitted = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_published = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_updated = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    body = RichTextUploadingField(
        blank=True,
        config_name="default",
        external_plugin_resources=[
            (
                "youtube",
                "/static/site_base/vendor/ckeditor_plugins/youtube/youtube/",
                "plugin.js",
            )
        ],
    )

    class Meta:
        """Meta definition for Article."""

        ordering = ["-date_published"]
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        """Unicode representation of Article."""
        return str(self.id) + " | " + self.title

    @property
    def last_updated(self):
        """Determins roughly the amount of time since an Article's last update
            and returns a pretty string.

        Returns:
            str: Description of time since last modification.
        """
        prefix = "Last updated about"
        if self.date_updated is None:
            return None
        else:
            last_updated_ago = (
                datetime.now(pytz.timezone(settings.TIME_ZONE)) - self.date_updated
            )
            if (last_updated_ago.days / 365) >= 1:
                return f"{prefix} {round(last_updated_ago.days / 365)} year(s) ago"
            elif (last_updated_ago.days / 30) >= 1:
                return f"{prefix} {round(last_updated_ago.days / 30)} month(s) ago"
            elif last_updated_ago.days >= 1:
                return f"{prefix} {last_updated_ago.days} day(s) ago"
            elif ((last_updated_ago.seconds / 60) / 60) >= 1:
                return f"{prefix} {round((last_updated_ago.seconds / 60) / 60)} hour(s) ago"
            elif (last_updated_ago.seconds / 60) >= 1:
                return f"{prefix} {round(last_updated_ago.seconds / 60)} minute(s) ago"
            else:
                return f"{prefix} less than a minute ago"
