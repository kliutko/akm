from django.urls import path
from .views import *



urlpatterns = [
    path('profile_update/', AccountsUpdate.as_view(), name='update'),
    path('<slug:acc_slug>/', Account.as_view(), name='account'),



]