# Generated by Django 2.1.5 on 2019-03-26 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0008_auto_20190325_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='botbase',
            name='telegram_chat_id',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
