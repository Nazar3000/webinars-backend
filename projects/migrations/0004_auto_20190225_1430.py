# Generated by Django 2.1.5 on 2019-02-25 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20190225_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autowebinar',
            name='project',
        ),
        migrations.RemoveField(
            model_name='autowebinarfakechatmessage',
            name='auto_webinar',
        ),
        migrations.RemoveField(
            model_name='webinar',
            name='created',
        ),
        migrations.RemoveField(
            model_name='webinar',
            name='updated',
        ),
        migrations.DeleteModel(
            name='AutoWebinar',
        ),
        migrations.DeleteModel(
            name='AutoWebinarFakeChatMessage',
        ),
    ]