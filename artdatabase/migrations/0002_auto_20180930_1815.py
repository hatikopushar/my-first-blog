# Generated by Django 2.1 on 2018-09-30 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artdatabase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='art',
            old_name='published_date',
            new_name='created',
        ),
    ]
