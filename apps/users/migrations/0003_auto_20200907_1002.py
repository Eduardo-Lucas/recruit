# Generated by Django 3.0.5 on 2020-09-07 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200907_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='company_name',
            field=models.CharField(default='company name', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='designation',
            field=models.CharField(default='designation', max_length=50),
        ),
    ]
