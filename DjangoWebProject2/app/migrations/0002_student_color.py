# Generated by Django 2.2.22 on 2021-06-01 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='color',
            field=models.CharField(default='white', max_length=50),
        ),
    ]