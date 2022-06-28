from django.db import models
from django.utils import timezone

class BugReport(models.Model):
    bug_url = models.URLField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    occured = models.DateTimeField(default=timezone.now)
    resolved = models.BooleanField(default=False)
