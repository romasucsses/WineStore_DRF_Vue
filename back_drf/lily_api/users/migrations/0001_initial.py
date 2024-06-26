# Generated by Django 5.0.1 on 2024-02-06 15:10

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=155, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=355)),
                ('name', models.CharField(max_length=155, null=True)),
                ('last_name', models.CharField(max_length=155, null=True)),
                ('date_joining', models.DateTimeField(default=datetime.datetime(2024, 2, 6, 15, 10, 22, 554962, tzinfo=datetime.timezone.utc))),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('user_shipping_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.shippinginfo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
