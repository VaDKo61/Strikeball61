# Generated by Django 4.1.3 on 2023-09-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday_games', '0009_alter_game_organizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='scenario',
            field=models.TextField(default='Будет позже', max_length=10000),
        ),
    ]
