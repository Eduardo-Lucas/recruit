from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    """
    This class is going to used to determine if an user is a Job Seeker or an Employer.
    If jobseeker is False, then it is an Employer
    """
    is_jobseeker = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default='some address')
    address1 = models.CharField(max_length=100, default='some address')
    address2 = models.CharField(max_length=100, default='some address')
    city = models.CharField(max_length=50, default='Rio de Janeiro')
    postal_code = models.CharField(max_length=10, default='41815-215')
    country = CountryField(default='Brazil')


class JobSeeker(models.Model):
    user = models.OneToOneField(CustomUser, related_name='jobseeker_profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Employer(models.Model):
    user = models.OneToOneField(CustomUser, related_name='employer_profile', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, default='company name')
    designation = models.CharField(max_length=50, default='designation')

    def __str__(self):
        return self.company_name
