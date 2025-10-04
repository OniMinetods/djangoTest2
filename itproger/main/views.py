from django.shortcuts import render
from django.http import JsonResponse

data = {
    'title': 'Главная страница',
  }

def index(request):
  return render(request, 'main/index.html', data)

def about(request):
  return render(request, 'main/about.html')

def image_list(request):
  images = [
    {'url': request.build_absolute_uri('/static/main/img/gleb_tdd.jpg'), 'alt': 'glebTdd'},
    {'url': request.build_absolute_uri('/static/main/img/suzuya.jpg'), 'alt': 'suzuya'},
    {'url': request.build_absolute_uri('/static/main/img/twitch_logo.png'), 'alt': 'twitchPidoras'}
  ]
  return JsonResponse(images, safe=False)
