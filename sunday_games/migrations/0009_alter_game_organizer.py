# Generated by Django 4.1.3 on 2023-09-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday_games', '0008_alter_game_scenario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='organizer',
            field=models.CharField(choices=[('STRIKE61', 'STRIKE61')], default='STRIKE61', max_length=50),
        ),
    ]
