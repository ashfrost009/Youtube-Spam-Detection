from django.db import models

class Url(models.Model):
    url = models.URLField(max_length=200)
