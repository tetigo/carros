# Generated by Django 4.2.5 on 2023-09-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_photo_car_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
    ]
