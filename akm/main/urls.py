from django.urls import path
from .views import *
from about.views import *
from main.views import *


urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),


]