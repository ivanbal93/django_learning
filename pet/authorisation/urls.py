from .views import authorisation

from django.urls import path


urlpatterns = [
    path('auth/', authorisation),
]
