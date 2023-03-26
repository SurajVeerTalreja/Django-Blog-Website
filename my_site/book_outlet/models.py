from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    is_bestselling = models.BooleanField(default=False)
    # db_index makes it more search friendly
    # Please make sure you don't add all fields as db_index as it will make system more complex
    slug = models.SlugField(default="", db_index=True, blank=True, null=False)

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.slug])

    def __str__(self):
        return f"{self.title} ({self.rating})"