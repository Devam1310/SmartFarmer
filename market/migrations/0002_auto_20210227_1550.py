# Generated by Django 3.1.7 on 2021-02-27 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='current_price',
            old_name='arrival_data',
            new_name='arrival_date',
        ),
    ]
