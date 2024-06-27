# Generated by Django 5.0.6 on 2024-06-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_orderinfo_total_sum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippinginfo',
            name='country',
        ),
        migrations.RemoveField(
            model_name='shippinginfo',
            name='street_address_2',
        ),
        migrations.AlterField(
            model_name='shippinginfo',
            name='state',
            field=models.CharField(default=None, max_length=155),
            preserve_default=False,
        ),
    ]
