from django.db import models
from django.urls import reverse


class Team(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=200, default='')
    logo = models.ImageField(default='', upload_to='team')
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('info_team', args=[self.slug])


class Player(models.Model):
    Men = 'M'
    Women = 'W'
    gender_choose = [
        (Men, 'Мужчина'),
        (Women, 'Женщина')
    ]
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=gender_choose, default='M')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.second_name} {self.first_name} '
