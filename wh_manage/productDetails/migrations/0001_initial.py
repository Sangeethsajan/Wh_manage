# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-16 03:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('AddressLine1', models.CharField(max_length=100)),
                ('AddressLine2', models.CharField(max_length=100)),
                ('PinCode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='productDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_Name', models.CharField(max_length=100)),
                ('rack_No', models.IntegerField()),
                ('price', models.IntegerField()),
                ('category_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productDetails.Category')),
                ('manufacturer_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productDetails.Manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='productPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rack', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='productSuggestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productDetails.productDetails')),
            ],
        ),
    ]
