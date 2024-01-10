from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from pytils.translit import slugify

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
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=gender_choose, default='M')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True, related_name='in_team')
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, related_name='info')
    phone = PhoneNumberField(region='RU', blank=True, null=True)
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'{self.user}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserInfo, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('profile_user', args=[self.slug])

    def get_url_edit(self):
        return reverse('edit_profile_user', args=[self.slug])
