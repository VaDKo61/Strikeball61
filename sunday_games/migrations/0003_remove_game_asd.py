# Generated by Django 4.1.3 on 2023-09-08 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sunday_games', '0002_game_asd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='asd',
        ),
    ]
