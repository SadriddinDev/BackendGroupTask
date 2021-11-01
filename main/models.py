from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    desciption = models.CharField(max_length=255, blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}-{self.name}"


class Deliver(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.BigIntegerField(default=0)
    deliver = models.ForeignKey(Deliver, on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    expired = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
