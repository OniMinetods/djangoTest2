from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def temperature(request):
  if request.method == 'POST':
    room = request.POST.get('room')
    temp = request.POST.get('temperature')
    data = [room, temp]
    return JsonResponse(data, safe=False)
  else:
    return JsonResponse({'error': 'Method not allowed'}, status=405)
