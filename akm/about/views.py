from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def about(request):
    portfolio = Portfolio.objects.all()
    data = {
        'portfolio': portfolio
    }


    return render(request, 'main/about.html', data)

def potfolio(request):

    return render(request, 'main/about.html')
