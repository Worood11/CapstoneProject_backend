from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Bookstore(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.URLField(blank=True , null=True)
    map_url = models.URLField(blank=True , null = True)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    bookstore = models.ForeignKey(Bookstore, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating must be between 1 (worst) and 5 (best)"
    )
    body = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.rating}⭐"