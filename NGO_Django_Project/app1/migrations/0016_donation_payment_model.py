# Generated by Django 3.0.5 on 2023-06-13 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_delete_transaction_tracking_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='donation_payment_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100)),
                ('paid', models.BinaryField(default=False)),
            ],
        ),
    ]
