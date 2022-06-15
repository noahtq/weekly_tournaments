from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True)
    location = models.CharField(max_length=100)
    event_datetime = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    registered_users = models.ManyToManyField(User, related_name="registeredusers", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})
