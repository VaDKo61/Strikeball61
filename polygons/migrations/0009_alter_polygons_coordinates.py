# Generated by Django 4.1.3 on 2023-09-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polygons', '0008_polygons_url_yandex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polygons',
            name='coordinates',
            field=models.CharField(default='', max_length=50),
        ),
    ]