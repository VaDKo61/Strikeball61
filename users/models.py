from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget

from team_player.models import Team


class UserInfo(models.Model):
    """Player"""
    Men = 'M'
    Women = 'W'
    gender_choose = [
        (Men, 'Мужчина'),
        (Women, 'Женщина')
    ]
    photo = models.ImageField(upload_to='user/', blank=True, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=gender_choose, default='M')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True, related_name='in_team')
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, related_name='info')
    phone = PhoneNumberField(region='RU', blank=True, null=True)

    def __str__(self):
        return f'{self.user}'
