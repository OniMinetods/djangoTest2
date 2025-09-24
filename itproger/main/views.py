from django.shortcuts import render

data = {
    'title': 'Главная страница',
  }

def index(request):
  return render(request, 'main/index.html', data)

def about(request):
  return render(request, 'main/about.html')
