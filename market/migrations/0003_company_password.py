# Generated by Django 3.1.7 on 2021-02-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20210227_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='password',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]