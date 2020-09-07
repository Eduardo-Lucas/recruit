# Generated by Django 3.0.5 on 2020-09-07 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200907_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='designation',
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='jobseeker_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='company name', max_length=100)),
                ('designation', models.CharField(default='designation', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
