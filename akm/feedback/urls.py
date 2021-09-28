from django.urls import path
from .views import *

urlpatterns = [
    path('', feedback, name='feedback'),
    path('map/', feedbackmap, name='feedbackmap'),


]