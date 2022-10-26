# Generated by Django 4.0.7 on 2022-09-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moreAdmin', '0017_payment_orderid_payment_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=150)),
                ('added_date', models.DateTimeField()),
                ('validtill', models.DateTimeField()),
                ('minimum_price', models.IntegerField()),
            ],
        ),
    ]