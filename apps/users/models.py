from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default='some address')
    address1 = models.CharField(max_length=100, default='some address')
    address2 = models.CharField(max_length=100, default='some address')
    city = models.CharField(max_length=50, default='Rio de Janeiro')
    country = CountryField(default='Brazil')

    def __str__(self):
        return self.email

    def get_full_name(self):
        self.full_name = self.first_name + self.last_name
