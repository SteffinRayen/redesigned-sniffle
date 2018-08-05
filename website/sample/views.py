from django.shortcuts import render
from django.http import HttpResponse
from .models import ClusterData, ModuleData, ProjectData, ErrorData
# https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
from django.urls import reverse_lazy
# https://stackoverflow.com/questions/10502135/django-queryset-to-dict-for-use-in-json
import json
from django.core.serializers.json import DjangoJSONEncoder

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
    dict_pair_cluster = ClusterData.objects.values_list()
    dict_pair_project = ProjectData.objects.values_list()
    dict_pair_module = ModuleData.objects.values_list()
    dict_pair_error = ErrorData.objects.values_list()
    context = {
        'cluster_data_pair': json.dumps(list(dict_pair_cluster), cls=DjangoJSONEncoder),
        'module_data_pair': json.dumps(list(dict_pair_project), cls=DjangoJSONEncoder),
        'project_data_pair': json.dumps(list(dict_pair_module), cls=DjangoJSONEncoder),
        'error_data_pair': json.dumps(list(dict_pair_error), cls=DjangoJSONEncoder),
    }
    return render(request, 'sample/ajaxTrial.html', context)


def upload(request):
    context = {}
    return render(request, 'sample/upload.html', context)


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the sample home page.</h1>")


def handler404(request, exception, template_name='404.html'):
    return render(request, '404.html', status=404)
