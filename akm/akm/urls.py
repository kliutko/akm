from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from news.views import *
from feedback.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', include('main.urls')),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('contact/', include('feedback.urls')),
    path('account/', include('account.urls')),
    path('about/', include('about.urls')),



]
