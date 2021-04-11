# Generated by Django 2.2.20 on 2021-04-10 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='tutor',
        ),
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='app.tutor'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]