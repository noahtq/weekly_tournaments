from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Event(models.Model):
    
    class EventTypes(models.TextChoices):
        BASKETBALL = '1', 'Basketball'
        SUPERSMASH = '2', 'Super Smash'
        FREERUNNING = '3', 'Freerunning'

    class EventStatus(models.TextChoices):
        UPCOMING = '1', 'Upcoming'
        ACTIVE = '2', 'Active'
        DONE = '3', 'Done'

    title = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=EventTypes.choices, default=EventTypes.BASKETBALL)
    description = models.TextField(default='', blank=True)
    location = models.CharField(max_length=100)
    event_datetime = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    registered_users = models.ManyToManyField(User, related_name="registeredusers", blank=True)
    max_users = models.IntegerField(default=10)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=EventStatus.choices, default=EventStatus.UPCOMING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})
