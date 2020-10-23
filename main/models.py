from django.db import models


# Create your models here.


class AppUsers(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.IntegerField()
    married = models.BooleanField()
