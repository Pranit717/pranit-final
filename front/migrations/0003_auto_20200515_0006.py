# Generated by Django 3.0.4 on 2020-05-14 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20200514_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='location',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='type',
        ),
    ]