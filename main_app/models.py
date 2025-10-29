from django.db import models

# Create your models here.

class Bookstore(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.URLField(blank=True , null=True)
    map_url = models.URLField(blank=True , null = True)

    def __str__(self):
        return self.name