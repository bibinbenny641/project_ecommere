# Generated by Django 4.0.7 on 2022-10-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moreAdmin', '0022_alter_user_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorders',
            name='orderstatus',
            field=models.CharField(default='Placed', max_length=50),
        ),
    ]
