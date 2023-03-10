# Generated by Django 4.1.7 on 2023-02-21 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Категория")),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="Описание"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Товара")),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default=None,
                        max_length=2000,
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=7, verbose_name="Цена"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="webapp.category",
                        verbose_name="category",
                    ),
                ),
            ],
        ),
    ]
