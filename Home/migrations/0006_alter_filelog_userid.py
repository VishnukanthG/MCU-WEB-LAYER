# Generated by Django 4.1.3 on 2022-12-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_filelog_delete_csv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filelog',
            name='userid',
            field=models.IntegerField(null=True),
        ),
    ]
