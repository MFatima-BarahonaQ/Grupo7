from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse("Hola Mundo. Te encuentras en la página de inicio del Linio Express")



# Create your views here.
