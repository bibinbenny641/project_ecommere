# Generated by Django 4.0.7 on 2022-09-24 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moreAdmin', '0010_alter_myorders_orderstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myorders',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='myorders',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='myorders',
            name='city',
        ),
        migrations.RemoveField(
            model_name='myorders',
            name='district',
        ),
        migrations.RemoveField(
            model_name='myorders',
            name='zip',
        ),
    ]