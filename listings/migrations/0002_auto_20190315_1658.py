# Generated by Django 2.1.7 on 2019-03-15 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='lsit_date',
            new_name='list_date',
        ),
    ]
