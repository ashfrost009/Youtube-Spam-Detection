from django.db import models

# Create your models here.
class URL(models.Model):
    link = models.fields.CharField(max_length=100)