# Generated by Django 3.0.4 on 2020-05-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_auto_20200515_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='location',
            field=models.CharField(blank=True, choices=[('Mumbai', 'Mumbai'), ('Pune', 'Pune'), ('Bangalore', 'Banaglore'), ('Hyderabad', 'Hyderabad'), ('Chennai', 'Chennai')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.CharField(blank=True, choices=[('Flat', 'Flat'), ('Bungalow', 'Bungalow'), ('PG/Hostel', 'PG/Hostel')], max_length=30, null=True),
        ),
    ]