# Generated by Django 5.0.6 on 2024-06-30 04:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qBank', '0015_alter_otp_table_expire_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='submission_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 30, 4, 53, 7, 507627, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='otp_table',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 30, 4, 55, 7, 507627, tzinfo=datetime.timezone.utc)),
        ),
    ]
