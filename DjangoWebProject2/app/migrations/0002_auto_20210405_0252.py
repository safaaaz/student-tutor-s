# Generated by Django 2.2.19 on 2021-04-04 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='idt',
            field=models.IntegerField(default=0),
        ),
    ]