# Generated by Django 3.2 on 2021-06-20 01:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_alter_temporder_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporder',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
