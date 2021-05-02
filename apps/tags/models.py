from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['name'], name='unique-tag')]

    def save(self, *args, **kwargs):
        self.name = self.name.lower().strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name