from django.db import models
from django.utils import timezone
from weekly_tournaments.urls import urlpatterns


class BugReport(models.Model):
    bug_url = models.URLField(max_length=200)
    description = models.TextField()
    instructions = models.TextField(blank=True)
    occured = models.DateTimeField(default=timezone.now)
    resolved = models.BooleanField(default=False)

