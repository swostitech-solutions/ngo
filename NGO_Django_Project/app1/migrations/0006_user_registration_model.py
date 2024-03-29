# Generated by Django 3.0.5 on 2023-05-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_delete_user_registration_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_registration_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.TextField(max_length=200)),
            ],
        ),
    ]
