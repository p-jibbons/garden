# Generated by Django 3.0.7 on 2020-06-27 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garden_app', '0007_plant_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='Image',
            new_name='image',
        ),
    ]
