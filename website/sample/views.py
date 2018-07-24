from django.shortcuts import render,render_to_response

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import ClusterData, ProjectData, ModuleData, ErrorData

def login(request):
    #template = loader.get_template('sample/login.html')
    #return HttpResponse("<h1>Hello, world. You're at the sample login.</h1>")
    context = {}
    #return HttpResponse(template.render(context, request))
    return render(request, 'sample/login.html', context)

def index(request):
    #Should display the home page with 3 options
    # Option 1 to search
    # Option 2 to Upload
    # Logout?
    #template = loader.get_template('login.html')
    return HttpResponse("<h1>Hello, world. You're at the sample home.</h1>")

def handler404(request, exception, template_name='404.html'):
    return render(request, '404.html', status=404)
