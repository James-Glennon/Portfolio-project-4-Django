# Generated by Django 3.2.20 on 2023-07-12 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20230709_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f4108df0c40> <django.db.models.query_utils.DeferredAttribute object at 0x7f4108df0ca0>', max_length=100),
        ),
    ]
