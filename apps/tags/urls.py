from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.tags.views import TagViewSet

router = routers.DefaultRouter()
router.register(r'tags', TagViewSet)

app_name = "tags"

urlpatterns = [
    path('', include(router.urls)),
]