from django.urls import path
from .views import *



urlpatterns = [
    path('<slug:acc_slug>/', Account.as_view(), name='account'),


]