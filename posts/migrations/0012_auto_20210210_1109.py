# Generated by Django 3.1.6 on 2021-02-10 11:09

import datetime
from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20210210_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 10, 11, 9, 8, 497976)),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=posts.models.upload_path),
        ),
    ]
