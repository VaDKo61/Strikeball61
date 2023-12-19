from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    """Form of registrations"""

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class UserAuthenticationForm(AuthenticationForm):
    """Form of authentication"""

    class Meta:
        model = User
