# Generated by Django 2.1.5 on 2019-02-25 15:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0005_auto_20190225_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinar',
            name='viewers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]