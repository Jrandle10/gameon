from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Game:
  def __init__(self, name, platform, description, release_date):
    self.name = name
    self.platform = platform
    self.description = description
    self.release_date = release_date

games = [
  Game('God Of War', 'Playstation', 'Kranos takes down all the gods', '2005'),
  Game('Madden 21', 'Xbox', 'NFL game', '2020'),
  Game('Fifa 21', 'Playstation', 'Soccer game', '2020'),
]

def home(request):
  return HttpResponse('<h1>Hello Gamer!</h1>')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  return render(request, 'games/index.html', {'games': games})