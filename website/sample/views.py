from django.shortcuts import render,render_to_response

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
def index(request):
    return HttpResponse("<h1>Hello, world. You're at the sample index.</h1>")

def handler404(request, exception, template_name='404.html'):
    return render(request, '404.html', status=404)
