from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction

from .models import CustomUser, JobSeeker, Employer


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class JobSeekerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        customuser = super().save(commit=False)
        customuser.is_jobseeker = True
        customuser.save()
        jobseeker = JobSeeker.objects.create(user=customuser)
        return customuser


class EmployerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

    def save(self, commit=True):
        customuser = super().save(commit=False)
        customuser.is_employer = True
        if commit:
            customuser.save()
        return customuser


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'address', 'address1', 'address2', 'city', 'country',
                  'data_joined', 'is_jobseeker']
        exclude = ['password', 'data_joined', 'last_login', 'is_superuser', 'groups',
                   'user_permissions', 'username', 'full_name', 'is_staff', 'is_active',
                   ]


class EmployerForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'address', 'address1', 'address2', 'city', 'country',
                  'data_joined', 'is_jobseeker']
        exclude = ['password', 'data_joined', 'last_login', 'is_superuser', 'groups',
                   'user_permissions', 'username', 'full_name', 'is_staff', 'is_active',
                   ]

