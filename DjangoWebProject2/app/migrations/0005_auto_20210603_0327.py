# Generated by Django 2.2.22 on 2021-06-03 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_merge_20210602_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='avgrate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tutor',
            name='numrate',
            field=models.IntegerField(default=0),
        ),
    ]