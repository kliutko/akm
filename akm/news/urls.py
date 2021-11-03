from django.urls import path
from .views import *
from about.views import *


urlpatterns = [
    path('', news, name='news'),
    path('cat/<slug:category_slug>/', show_category, name='category'),
    path('<slug:news_slug>/', show_news, name='news')

]