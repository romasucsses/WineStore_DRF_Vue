# Generated by Django 5.0.1 on 2024-02-06 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=355)),
                ('image', models.ImageField(upload_to='img/%y/%m/%d/')),
                ('price', models.FloatField()),
                ('description', models.TextField(blank=True)),
                ('date_added', models.DateField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('slug_url', models.SlugField(max_length=355, unique=True, verbose_name='URL')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('stars_count', models.IntegerField(null=True)),
                ('review', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
        ),
    ]
