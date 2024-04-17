from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='photos/category', blank=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_url(self):
        
        # using reverse function, from store app takes url name='product_by_category' & Category Slug       
        return reverse('product_by_category', args=[self.slug])
    