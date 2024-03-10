#  This is where all the application models are stored.
# import datetime
from django.db import models
# from django.utils.text import slugify

class Car(models.Model):
    model = models.CharField(max_length=100)

    def __str__(self):
        return self.model

# class Car(models.Model):
#     name = models.CharField(max_length=255)
#     km = models.IntegerField()
#     h = models.IntegerField()
#     year = models.IntegerField()
#     date = models.DateField(default=datetime.date.today)
#     slug = models.SlugField(unique=True)

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args, **kwargs)

#     def get_absolute_url(self):
#         return f'/cars/{self.slug}/'
