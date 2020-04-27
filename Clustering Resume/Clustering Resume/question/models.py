from django.conf import settings
from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=200)
    question = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Growth(models.Model):
    title = models.CharField(max_length=200)
    question = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Personality(models.Model):
    title = models.CharField(max_length=200)
    question = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Other(models.Model):
    title = models.CharField(max_length=200)
    question = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
