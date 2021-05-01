from django.contrib import admin
from .models import Gif

# Register your models here.
@admin.register(Gif)
class GifAdmin(admin.ModelAdmin):
  list_display = [field.name for field in Gif._meta.get_fields()]
