from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    countryCode = models.CharField(max_length=3, unique=True)
    id = models.IntegerField(primary_key=True)
    groupId = models.IntegerField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
