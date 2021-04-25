from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.gifs import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

app_name = "gifs"

urlpatterns = [
    path('', include(router.urls)),
]