# Generated by Django 3.2 on 2021-04-18 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budgeteerApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date',
            old_name='date',
            new_name='day',
        ),
    ]
