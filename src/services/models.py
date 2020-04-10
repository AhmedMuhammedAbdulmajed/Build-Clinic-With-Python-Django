from django.db import models

# Create your models here.
class services(models.Model):
    name =  models.CharField(max_length=50)
    detial =  models.CharField(max_length=250)

    def __str__(self):
        return self.name