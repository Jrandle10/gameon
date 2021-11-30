from django.db.models import fields
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game, Photo
import uuid
import boto3
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def games_index(request):
  games = Game.objects.filter(user=request.user)
  return render(request, 'games/index.html', {'games': games })

@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'games/detail.html', { 'game': game })

class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = '__all__'
  success_url = '/games/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = ['platform', 'description']

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('games_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)


S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'game-on-26'


def add_photo(request, game_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, game_id=game_id)
      game_photo = Photo.objects.filter(game_id=game_id)
      if game_photo.first():
        game_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('games_detail', game_id=game_id)

