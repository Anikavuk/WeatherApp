from django.db import models


# Create your models here.
class Users(models.Model):
    # id = models.IntegerField()
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=250)

class Locations (models.Model):
    name = models.CharField(max_length=50)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
