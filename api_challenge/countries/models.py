from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=3, unique=True)
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
