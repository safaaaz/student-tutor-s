# Generated by Django 2.2.20 on 2021-04-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210410_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='courses',
            field=models.CharField(default='', max_length=100),
        ),
    ]
