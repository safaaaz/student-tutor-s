# Generated by Django 2.2.20 on 2021-04-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20210422_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='chart',
            field=models.ManyToManyField(to='app.tutor'),
        ),
    ]