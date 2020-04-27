from django.conf import settings
from django.db import models
from django.utils import timezone


class Introduces(models.Model):
    motive = models.CharField(max_length=200)
    dream = models.CharField(max_length=200)
    growth = models.CharField(max_length=200)
    PAC = models.CharField(max_length=200)
    activities = models.CharField(max_length=200)

    @property
    def __str__(self):
        return self.motive

