from django.shortcuts import render
from django.http import HttpResponse
from .models import ClusterData, ModuleData, ProjectData, ErrorData
from django.urls import reverse_lazy #https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
# Create your views here.

def search(request):
    all_cluster_data = ClusterData.objects.all()
    all_module_data = ModuleData.objects.all()
    all_project_data = ProjectData.objects.all()
    all_error_data = ErrorData.objects.all()
    context = {
        'all_cluster_data' : all_cluster_data,
        'all_module_data' : all_module_data,
        'all_project_data' : all_project_data,
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
