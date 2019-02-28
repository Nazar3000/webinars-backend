# Generated by Django 2.1.5 on 2019-02-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190226_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=2048)),
                ('ip_address', models.GenericIPAddressField()),
                ('country', models.CharField(max_length=64)),
                ('region', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Device Data',
                'verbose_name_plural': 'Device Data instances',
            },
        ),
    ]
