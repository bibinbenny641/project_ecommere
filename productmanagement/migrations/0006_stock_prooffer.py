# Generated by Django 4.0.7 on 2022-10-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0005_alter_stock_category_alter_stock_subcatname'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='proOffer',
            field=models.IntegerField(default=5),
        ),
    ]
