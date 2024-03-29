# Generated by Django 3.0.5 on 2023-06-04 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_contact_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cat_id', models.CharField(max_length=40)),
                ('post_id', models.CharField(max_length=30)),
                ('donet_amount', models.CharField(max_length=40)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
