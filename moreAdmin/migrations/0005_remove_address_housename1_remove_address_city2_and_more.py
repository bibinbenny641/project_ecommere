# Generated by Django 4.0.7 on 2022-09-20 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moreAdmin', '0004_alter_address_housename1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='Housename1',
        ),
        migrations.RemoveField(
            model_name='address',
            name='city2',
        ),
        migrations.RemoveField(
            model_name='address',
            name='district2',
        ),
        migrations.RemoveField(
            model_name='address',
            name='zipcode2',
        ),
    ]