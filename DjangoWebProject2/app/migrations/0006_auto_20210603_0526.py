# Generated by Django 2.2.23 on 2021-06-03 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210602_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='image',
            field=models.ImageField(null=True, upload_to='media/images', verbose_name=''),
        ),
    ]
