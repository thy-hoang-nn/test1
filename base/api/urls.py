from .views import UserRegisterView
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('api/register/', UserRegisterView.as_view(), name='register'),
]
