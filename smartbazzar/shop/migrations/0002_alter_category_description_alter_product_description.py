# Generated by Django 5.1.4 on 2024-12-21 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=400),
        ),
    ]
