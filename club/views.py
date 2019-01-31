from django.shortcuts import render
from .models import Resource
# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def resourcetype (request):
    resource_list= Resource.objects.all()
    return render(request, 'club/types.html', {'resource_list': resource_list})