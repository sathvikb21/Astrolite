from django.db import models


class UserDetail(models.Model):
    username = models.CharField(max_length=25, unique=True)
    total_trips = models.IntegerField(default=0)
    upcoming_trips = models.IntegerField(default=0)
    total_distance = models.IntegerField(default=0)
    total_cost = models.IntegerField(default=0)
