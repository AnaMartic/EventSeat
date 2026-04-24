from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()

class Table(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    number = models.IntegerField()
    seats = models.IntegerField()
    shape = models.CharField(max_length=20)  # okrugao ili četvrtast

class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    table = models.ForeignKey(Table, null=True, blank=True, on_delete=models.SET_NULL)    