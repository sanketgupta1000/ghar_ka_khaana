"""
URL configuration for ghar_ka_khaana project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from user.views import landingpage_view, logout_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foodie/', include('foodie.urls')),
    path('kitchen/', include("kitchen.urls")),
    path('', landingpage_view, name='landingpage'),
    path('logout', logout_request, name='logout'),
]
