# Generated by Django 4.1.3 on 2023-09-07 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team_player', '0003_remove_team_players_player_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_team', to='team_player.team'),
        ),
    ]
