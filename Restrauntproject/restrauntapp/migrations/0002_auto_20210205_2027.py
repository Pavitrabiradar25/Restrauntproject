# Generated by Django 3.1 on 2021-02-05 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restrauntapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooddetails',
            old_name='foodtype',
            new_name='citi',
        ),
    ]