# Generated by Django 4.2.6 on 2023-10-10 21:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('holder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
