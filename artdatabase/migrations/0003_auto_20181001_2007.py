# Generated by Django 2.1 on 2018-10-02 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artdatabase', '0002_auto_20180930_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='last_name',
        ),
    ]
