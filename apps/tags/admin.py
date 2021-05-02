from django.contrib import admin
from .models import Tag

@admin.register(Tag)
class GifAdmin(admin.ModelAdmin):
    list_display = ['name']
