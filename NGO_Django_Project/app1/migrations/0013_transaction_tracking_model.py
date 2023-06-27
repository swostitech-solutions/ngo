# Generated by Django 3.0.5 on 2023-06-06 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_delete_transaction_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction_tracking_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=50, null=True)),
                ('post_name', models.CharField(max_length=50, null=True)),
                ('customer_name', models.CharField(max_length=70)),
                ('amount', models.IntegerField()),
                ('donate_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
