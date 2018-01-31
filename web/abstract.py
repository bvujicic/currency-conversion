"""
Abstract inheritance models.
"""
from django.db import models


class TimestampModel(models.Model):
    """
    Abstract models for timestamps.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True