from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
  name = models.CharField(max_length=100)
  platform = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse('games_detail', kwargs={'game_id': self.id})


class Photo(models.Model):
  url = models.CharField(max_length=250)
  game = models.OneToOneField(Game, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for game_id: {self.game_id} @{self.url}"
  
