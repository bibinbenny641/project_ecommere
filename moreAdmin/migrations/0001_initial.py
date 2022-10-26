# Generated by Django 4.0.7 on 2022-09-20 04:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productmanagement', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('fullname', models.CharField(blank=True, max_length=200, null=True)),
                ('phoneno', models.CharField(max_length=10, null=True, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Myorders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('amount', models.CharField(max_length=10)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.BigIntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('status', models.BooleanField(default=True)),
                ('totalamount', models.IntegerField()),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productmanagement.stock')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]