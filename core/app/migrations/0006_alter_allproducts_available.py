# Generated by Django 3.2.12 on 2023-02-08 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20230208_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allproducts',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]