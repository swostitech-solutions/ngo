# Generated by Django 3.0.5 on 2023-06-17 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_donation_payment_model_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation_payment_model',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
