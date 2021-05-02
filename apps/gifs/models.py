from django.db import models
from django.utils.crypto import get_random_string
import os
from apps.tags.models import Tag
from django.contrib.auth.models import User


GIF_STATUS = (
    ('P', 'pending'),
    ('A', 'accepted'),
    ('R', 'rejected'),
)

class Gif(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=GIF_STATUS, default='P')
    uid = models.CharField(max_length=32, blank=True)
    gif = models.ImageField(upload_to='gifs/%Y/%m')
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['uid'], name='unique-uid')]
        
    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = get_random_string(length=32)
            self._rename()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        filepath = self.gif.path
        super().delete(*args, **kwargs)
        if os.path.exists(filepath):
            os.remove(filepath)

    def _rename(self):
        self.gif.name = f"{self.uid}.gif"