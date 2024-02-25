from django.urls import path
from . import views

app_name="kitchen"

urlpatterns = [
    # path for account creation
    path('register/', views.register_view, name="register"),
    # path for login
    path('login/', views.login_view, name="login"),
    path('', views.index, name='index'),
]