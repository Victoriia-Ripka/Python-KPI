#  This is where all the application models are stored.
from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=100)

    def __str__(self):
        return self.model