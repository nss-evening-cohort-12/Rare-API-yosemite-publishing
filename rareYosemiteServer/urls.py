from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rareapi.views import register_user, login_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
