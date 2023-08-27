from django.db import models


class Product(models.Model):
    id_ = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=350, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField()
    # image = models.ImageField(path=)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    ...
