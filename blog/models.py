from django.db import models
from django.contrib.auth import get_user_model

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
