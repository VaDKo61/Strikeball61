# Generated by Django 4.1.3 on 2023-09-01 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polygons', '0006_alter_polygons_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='polygons',
            name='image_full',
            field=models.ImageField(default='', upload_to='polygons/full'),
        ),
    ]
