# Generated by Django 4.2.6 on 2023-10-11 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holder', '0002_item_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
