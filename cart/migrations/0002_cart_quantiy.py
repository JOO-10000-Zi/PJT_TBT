# Generated by Django 3.2.13 on 2022-11-18 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantiy',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]