# Generated by Django 4.1.5 on 2023-04-08 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentinfo',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 8, 15, 44, 44, 712970)),
        ),
    ]