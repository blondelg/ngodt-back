from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.gifs.views import GifViewSet

router = routers.DefaultRouter()
router.register(r'gifs', GifViewSet)

app_name = "gifs"

urlpatterns = [
    path('', include(router.urls)),
]