"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from data.urls import router as data_router

from authorisation.urls import urlpatterns as auth_urlpatterns

from .views import main_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('', include('social_django.urls', namespace='social')),
    path('debug/', include('debug_toolbar.urls')),
]

urlpatterns += data_router.urls
urlpatterns += auth_urlpatterns

