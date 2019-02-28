# Generated by Django 2.1.5 on 2019-02-28 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_devicedata'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicedata',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='devicedata',
            name='country',
            field=models.CharField(default='United Kingdom', max_length=64),
        ),
        migrations.AlterField(
            model_name='devicedata',
            name='region',
            field=models.CharField(default='London', max_length=64),
        ),
    ]
