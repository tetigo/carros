# Generated by Django 4.2.5 on 2023-10-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_carinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
