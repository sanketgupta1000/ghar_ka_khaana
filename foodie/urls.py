from django.urls import path
from . import views

app_name = 'foodie'

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login_request, name='login'),
]