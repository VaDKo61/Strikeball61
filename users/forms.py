from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

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
        exclude = {'password', 'last_login', 'is_active', 'is_staff', 'is_active', 'is_superuser', 'groups',
                   'user_permissions', 'username', 'date_joined'}


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
