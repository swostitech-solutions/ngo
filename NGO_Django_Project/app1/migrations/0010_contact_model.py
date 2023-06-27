# Generated by Django 3.0.5 on 2023-05-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_delete_custom_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=70)),
                ('address', models.CharField(max_length=70)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
