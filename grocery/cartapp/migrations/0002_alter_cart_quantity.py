# Generated by Django 4.1.3 on 2023-07-08 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
