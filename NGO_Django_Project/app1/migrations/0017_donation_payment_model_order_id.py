# Generated by Django 3.0.5 on 2023-06-17 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_donation_payment_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation_payment_model',
            name='order_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]