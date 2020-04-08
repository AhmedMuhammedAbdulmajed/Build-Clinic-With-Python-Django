from django.db import models

# Create your models here.
class services(models.Model):
    name = models.CharField(max_length=60)
    detial = models.TextField()

    def __str__(self):
        return self.name
