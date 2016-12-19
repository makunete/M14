from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Esto es el indice de mi aplicacion forum.")
# Create your views here.
