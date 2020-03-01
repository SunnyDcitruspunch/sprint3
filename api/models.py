from django.db import models


class Category(models.Model):
    title = models.TextField()


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.TextField()
    description = models.TextField()
    filename = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
