# Generated by Django 4.1.3 on 2023-09-27 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polygons', '0014_alter_polygons_lat_alter_polygons_lon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='polygons',
            name='image_full',
        ),
    ]
