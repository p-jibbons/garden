# Generated by Django 3.0.7 on 2020-07-07 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden_app', '0012_arduinopin_environmental_dimension'),
    ]

    operations = [
        migrations.AddField(
            model_name='arduinopin',
            name='is_collecting',
            field=models.BooleanField(default=False),
        ),
    ]