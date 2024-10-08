# Generated by Django 5.0.6 on 2024-06-28 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qBank', '0004_alter_otp_table_expire_time_alter_otp_table_otp_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choice_list_id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='reference_id',
        ),
        migrations.AddField(
            model_name='question',
            name='chapter_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_1',
            field=models.TextField(default='No choice submitted'),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_2',
            field=models.TextField(default='No choice submitted'),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_3',
            field=models.TextField(default='No choice submitted'),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_4',
            field=models.TextField(default='No choice submitted'),
        ),
        migrations.AddField(
            model_name='question',
            name='module_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='question_title',
            field=models.TextField(default='No title submitted'),
        ),
        migrations.AddField(
            model_name='question',
            name='sub_topic_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='topic_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='otp_table',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 28, 11, 58, 43, 519230, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='choice_list',
        ),
        migrations.DeleteModel(
            name='question_reference',
        ),
    ]
