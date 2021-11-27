from django.shortcuts import render


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
  Game('Fifa 21', 'Playstation', 'MLB soccer game', '2020'),
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  return render(request, 'games/index.html', {'games': games})