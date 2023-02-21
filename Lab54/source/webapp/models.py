from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Категория')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')


class Product(models.Model):
    category = models.ForeignKey(to=Category, related_name='products', verbose_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Товара')
    description = models.TextField(max_length=2000, null=True, blank=True, default=None, verbose_name='Описание')
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name
