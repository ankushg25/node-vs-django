from django.urls import path
from .views import get_request, post_request

urlpatterns = [
    path('login', get_request),
    path('post', post_request),
]

