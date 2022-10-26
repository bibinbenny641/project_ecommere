# Generated by Django 4.0.7 on 2022-09-26 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moreAdmin', '0014_myorders_orderdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentid', models.CharField(max_length=150)),
                ('paymentmethod', models.CharField(max_length=100)),
                ('totalamount', models.IntegerField()),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moreAdmin.myorders')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]