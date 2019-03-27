# Generated by Django 2.1.5 on 2019-03-27 11:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chains', '0005_message_sent_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sent_to',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]