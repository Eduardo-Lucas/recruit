from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'address', 'address1', 'address2', 'city', 'country',
                  'data_joined']
        exclude = ['password', 'data_joined', 'last_login', 'is_superuser', 'groups',
                   'user_permissions', 'username', 'full_name', 'is_staff', 'is_active',
                   ]
