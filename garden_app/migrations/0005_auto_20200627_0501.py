# Generated by Django 3.0.7 on 2020-06-27 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden_app', '0004_auto_20200627_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='light_needs',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=2),
        ),
        migrations.AlterField(
            model_name='plant',
            name='temperature_needs',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=2),
        ),
        migrations.AlterField(
            model_name='plant',
            name='water_needs',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=2),
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
