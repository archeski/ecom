# Generated by Django 2.0.7 on 2018-07-24 06:30

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')], default=0, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, verbose_name='phone number'),
        ),
        migrations.AddField(
            model_name='profile',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='postal code'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='address'),
        ),
    ]
