import re

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from users.models import UserInfo


class UserRegistrationForm(UserCreationForm):
    """Form of registrations"""

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class UserAuthenticationForm(AuthenticationForm):
    """Form of authentication"""

    class Meta:
        model = User


class UserEditForm(forms.ModelForm):
    """Form of edit user"""

    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email'}

    def clean_email(self):
        email = self.cleaned_data['email']
        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
        if re.match(pattern, email) is not None:
            return email
        else:
            raise ValidationError('Введен не корректный email')


class UserInfoEditForm(forms.ModelForm):
    """Form of edit user"""

    class Meta:
        model = UserInfo
        exclude = {'slug', 'user'}
        labels = {
            'photo': 'Фото',
            'age': 'Возраст',
            'gender': 'Пол',
            'team': 'Команда',
            'phone': 'Телефон',
        }


class UserPasswordReset(PasswordResetForm):
    pass
