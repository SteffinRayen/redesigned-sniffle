from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    context = {}
    return render(request, 'sample/login.html', context)

def search(request):
    context = {}
    return render(request, 'sample/search.html', context)

def index(request):
    return HttpResponse("<h1>Hello, world. You're at the sample home.</h1>")

def handler404(request, exception, template_name='404.html'):
    return render(request, '404.html', status=404)
