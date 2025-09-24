from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView
from django.http import JsonResponse

def news_home(request):
  news = Articles.objects.order_by('-date')   # [:2] вывести первые 2 записи
  return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):           # Класс для обработки шаблона
  model = Articles                          
  template_name = 'news/details_view.html'  
  context_object_name = 'article'           # Ключ по которому идет передача объекта внутрь шаблона

def create(request):
  error = ''
  if request.method == 'POST':
    form = ArticlesForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
    else:
      error = 'Форма была неверной'

  form = ArticlesForm()
  data = {
    'form': form,
    'error': error
  }

  return render(request, 'news/create.html', data);

def getData(request):
  if request.method == 'GET':
    data = Articles.objects.all().values()
    data = list(data)

    return JsonResponse(data, safe=False)
  return JsonResponse({'error': 'Method not allowed'}, status=405)

def getDataNumber(request, pk):
  data = Articles.objects.filter(pk=pk).values().first()
  return JsonResponse(data)