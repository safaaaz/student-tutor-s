# Generated by Django 2.2.24 on 2021-06-04 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210604_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]
