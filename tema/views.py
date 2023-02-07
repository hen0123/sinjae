from django.shortcuts import render

# Create your views here.

def course1(request):
    return render(request, 'tema/course1.html')
