# Generated by Django 4.1.3 on 2023-09-07 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polygons', '0008_polygons_url_yandex'),
        ('sunday_games', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Games',
            new_name='Game',
        ),
    ]
