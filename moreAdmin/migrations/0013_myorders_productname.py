# Generated by Django 4.0.7 on 2022-09-26 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moreAdmin', '0012_myorders_address_myorders_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorders',
            name='productname',
            field=models.CharField(default=11, max_length=100),
            preserve_default=False,
        ),
    ]
