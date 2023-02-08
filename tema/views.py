from django.shortcuts import render

# Create your views here.

def tema1(request):
    return render(request, 'tema/tema1.html')


def tema2(request):
    return render(request, 'tema/tema2.html')

def tema3(request):
    return render(request, 'tema/tema3.html')

def tema4(request):
    return render(request, 'tema/tema4.html')
