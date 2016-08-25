from django.db import models

# Create your models here.

class User(models.Model):

    firstName =  models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)
    eMail = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class UserEvent(models.Model):

    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    eventID = models.ForeignKey(Event, on_delete=models.CASCADE)

class Event(models.Model):

    venueId = models.ForeignKey(Venue, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    city = models.CharField(max_length=20)
    beginTime = models.DateTimeField('Start Time')
    endTime = models.DateTimeField('End Time')

class Venue(models.Model):

    name = models.CharField(max_length=200)
    streetAddress = models.CharField(max_length=300)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipCode = models.IntergerField(default=0)
    capacity = models.IntegerField(default=0)
    contact = models.CharField(max_length=30)
