"""
Defines forms for this app
"""

from django import forms


class UploadFile(forms.Form):
    """UploadFile definition."""

    name = forms.CharField(max_length=200, required=False)
    file = forms.FileField()
