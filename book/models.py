from django.db import models
class Book(models.Model):
    # soton tarif mikone
    title = models.CharField(max_length = 225)
    author = models.CharField(max_length=255)
    published_year = models.DateField()

# Create your models here.
