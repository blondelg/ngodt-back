from django.contrib import admin
from .models import Gif

@admin.register(Gif)
class GifAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'uid', 'gif']
    readonly_fields = ['uid']
    filter_horizontal = ['tags']