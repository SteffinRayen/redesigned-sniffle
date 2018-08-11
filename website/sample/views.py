from django.shortcuts import render
from django.http import HttpResponse
from .models import ClusterData, ModuleData, ProjectData, ErrorData
# https://stackoverflow.com/questions/39390927/convert-model-objects-all-to-json-in-python-using-django
from django.core import serializers

# Create your views here.


def search(request):
    all_cluster_data = ClusterData.objects.all()
    all_module_data = ModuleData.objects.all()
    all_project_data = ProjectData.objects.all()
    all_error_data = ErrorData.objects.all()

    context = {
        'cluster_data': all_cluster_data,
        'module_data': all_module_data,
        'project_data': all_project_data,
        'error_data': all_error_data,
    }
    return render(request, 'sample/search.html', context)


def ajax(request):
    all_cluster_data = ClusterData.objects.all()
    all_module_data = ModuleData.objects.all()
    all_project_data = ProjectData.objects.all()
    all_error_data = ErrorData.objects.all()
    context = {
        'cluster_data' : serializers.serialize("json", all_cluster_data),
        'project_data' : serializers.serialize("json", all_project_data),
        'module_data' : serializers.serialize("json", all_module_data),
        'error_data' : serializers.serialize("json", all_error_data),
    }
    return render(request, 'sample/ajaxTrial.html', context)


def upload(request):
    context = {}
    return render(request, 'sample/upload.html', context)


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the sample home page.</h1>")


def handler404(request, exception, template_name='404.html'):
    return render(request, '404.html', status=404)
