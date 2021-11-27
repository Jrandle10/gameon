from django.db import models

# Create your models here.

class Game(models.Model):
  name = models.CharField(max_length=100)
  platform = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  releasedate = models.DateField