# Generated by Django 4.1.3 on 2023-10-05 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday_games', '0012_delete_gameimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='result_foto',
            field=models.CharField(default='', max_length=500),
        ),
    ]
