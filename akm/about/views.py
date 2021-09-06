from django.shortcuts import render
from .models import *

# Create your views here.
def about(request):
    portfolio = Portfolio.objects.all()
    data = {
        'portfolio': portfolio
    }


    return render(request, 'about/about.html')

def potfolio(request):

    return render(request, 'about/about.html')
