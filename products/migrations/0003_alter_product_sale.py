# Generated by Django 3.2.13 on 2022-11-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20221115_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale',
            field=models.IntegerField(),
        ),
    ]
