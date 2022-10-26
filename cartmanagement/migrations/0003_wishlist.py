# Generated by Django 4.0.7 on 2022-09-24 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0001_initial'),
        ('cartmanagement', '0002_rename_user_cart_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=200)),
                ('price', models.IntegerField(null=True)),
                ('image', models.ImageField(upload_to='pics')),
                ('description', models.CharField(max_length=150)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productmanagement.stock')),
            ],
        ),
    ]