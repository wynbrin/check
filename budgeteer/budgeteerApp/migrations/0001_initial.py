# Generated by Django 3.2 on 2021-04-17 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0)),
                ('month', models.IntegerField(default=0)),
                ('date', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.IntegerField(default=0)),
                ('expenses', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=500)),
                ('reoccurring', models.BooleanField(default=0)),
                ('essential', models.BooleanField(default=0)),
                ('category', models.IntegerField(default=0)),
                ('purchase_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgeteerApp.date')),
            ],
        ),
    ]
