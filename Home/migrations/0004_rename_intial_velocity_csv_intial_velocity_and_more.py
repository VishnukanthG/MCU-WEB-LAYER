# Generated by Django 4.1.3 on 2022-12-03 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_rename_intvelocity_csv_intial_velocity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csv',
            old_name='Intial_velocity',
            new_name='intial_velocity',
        ),
        migrations.RenameField(
            model_name='csv',
            old_name='Time_taken',
            new_name='time_taken',
        ),
    ]
