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
    phone_number = models.CharField(max_length=20, default='55 71 9999-9999')
    postal_code = models.CharField(max_length=10, default='41815-215')
    country = CountryField(default='BR')


class JobSeeker(models.Model):
    user = models.OneToOneField(CustomUser, related_name='jobseeker_profile', on_delete=models.CASCADE)
    email = models.EmailField(max_length=20, default='example@gmail.com')
    location = models.CharField(max_length=100, default='Salvador')
    resume = models.TextField(max_length=500, null=True, blank=True)
    cover_letter = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.user


class Employer(models.Model):
    user = models.OneToOneField(CustomUser, related_name='employer_profile', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, default='company name')
    designation = models.CharField(max_length=50, default='Employer')

    def __str__(self):
        return self.company_name


MEDIA_TYPE_CHOICES = (
    ('Resume', 'Resume'),
    ('Cover Letter', 'Cover Letter'),
    ('Video', 'Video'),
)


class MediaFile(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=MEDIA_TYPE_CHOICES)
    file = models.FileField(upload_to='documents', default='')


class Skill(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50, default='Python')


class Reference(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    link_reference = models.URLField(max_length=100, default='github.com')


