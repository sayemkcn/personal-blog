# Generated by Django 2.0.3 on 2018-03-31 21:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_comment_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 31, 21, 42, 27, 358305)),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 31, 21, 42, 27, 356817)),
        ),
    ]