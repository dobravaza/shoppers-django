from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class Product(models.Model):
        cateegory = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
        name = models.CharField(max_length=255)
        slug = models.SlugField(max_length=255, unique=True)
        description = models.TextField(blank=True)
        price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


        created_at = models.DateTimeField(auto_now_add=True)

        class Meta:
            ordering = ('-created_at',)


        def __str__(self):
            return self.name