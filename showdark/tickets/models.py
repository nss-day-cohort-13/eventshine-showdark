from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):

    name = models.CharField(max_length=200)
    streetAddress = models.CharField(max_length=300)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipCode = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)
    contact = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Event(models.Model):

    venueId = models.ForeignKey(Venue, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    city = models.CharField(max_length=20)
    beginTime = models.DateTimeField('Start Time')
    endTime = models.DateTimeField('End Time')

    def __str__(self):
        return self.name


class UserEvent(models.Model):

    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)
