from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("Home 1")

def contato(request):
    return HttpResponse("Contato 1")

def sobre(request):
    return HttpResponse("Sobre 1")