# Generated by Django 5.0.6 on 2024-06-28 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qBank', '0006_alter_otp_table_expire_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp_table',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 28, 12, 51, 35, 578154, tzinfo=datetime.timezone.utc)),
        ),
    ]
