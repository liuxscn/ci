from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('rango says ok')

def home(request):
    return render(request, 'index.html')