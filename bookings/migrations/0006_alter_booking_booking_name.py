# Generated by Django 3.2.20 on 2023-07-13 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_alter_booking_booking_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f965d1b1e20> <django.db.models.query_utils.DeferredAttribute object at 0x7f965d1b1e80>', max_length=100),
        ),
    ]
