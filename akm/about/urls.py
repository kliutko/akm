from django.urls import path
from .views import *
from about.views import *


urlpatterns = [
    path('', about, name='about'),
    # path('', portfolio, name='portfolio'),
    path('<slug:portfolio_slug>/', show_portfolio, name='show_portfolio'),
    path('cat/<slug:category_slug>/', show_category_portfolio, name='show_category_portfolio'),



]