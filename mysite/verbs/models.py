from django.db import models

class Verbs(models.Model):
    verb = models.CharField(max_length=50)
    meaning = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=50)
