# Generated by Django 4.1.3 on 2023-09-15 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday_games', '0006_remove_game_foto_games_game_foto_scenario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='scenario',
            field=models.CharField(max_length=10000),
        ),
    ]