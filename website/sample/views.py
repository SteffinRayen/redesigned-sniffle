from django.shortcuts import render
from django.http import HttpResponse
from .models import ClusterData, ModuleData, ProjectData, ErrorData
# Create your views here.

def search(request):
    all_error_data = ErrorData.objects.all()
    context = {
        'all_error_data' : all_error_data,
    }
    return render(request, 'sample/search.html', context)

def upload(request):
    context = {}
    return render(request, 'sample/upload.html', context)

def index(request):
    return HttpResponse("<h1>Hello, world. You're at the sample home page.</h1>")

def handler404(request, exception, template_name='404.html'):
    return render(request, '404.html', status=404)
