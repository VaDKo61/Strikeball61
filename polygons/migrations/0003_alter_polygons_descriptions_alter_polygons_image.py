# Generated by Django 4.1.3 on 2023-08-30 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polygons', '0002_polygons_coordinates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polygons',
            name='descriptions',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='polygons',
            name='image',
            field=models.ImageField(upload_to='polygons/'),
        ),
    ]
