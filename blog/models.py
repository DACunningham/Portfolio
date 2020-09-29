from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import datetime
import pytz

# Create your models here.
class Article(models.Model):
    """Model definition for Article."""

    # TODO: Define fields here
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250, blank=True)
    date_submitted = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_published = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_updated = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    body = models.TextField()

    class Meta:
        """Meta definition for Article."""

        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        """Unicode representation of Article."""
        return str(self.id) + " | " + self.title

    @property
    def last_updated(self):
        if self.date_updated is None:
            return self.date_published
        else:
            last_upd = (
                datetime.now(pytz.timezone(settings.TIME_ZONE)) - self.date_updated
            )
            return last_upd
