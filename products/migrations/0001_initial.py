# Generated by Django 5.0.3 on 2024-03-21 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Product category',
                'verbose_name_plural': 'Product categories',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=50)),
                ('product_description', models.TextField()),
                ('product_count', models.IntegerField()),
                ('product_price', models.FloatField()),
                ('product_image', models.FileField(upload_to='product_images')),
                ('product_created_at', models.DateTimeField(auto_now_add=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categorymodel')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
