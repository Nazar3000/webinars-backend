# Generated by Django 2.1.5 on 2019-03-25 16:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chains', '0003_auto_20190311_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageaudio',
            name='message',
        ),
        migrations.RemoveField(
            model_name='messagebutton',
            name='message',
        ),
        migrations.RemoveField(
            model_name='messagedelay',
            name='message',
        ),
        migrations.RemoveField(
            model_name='messagefile',
            name='message',
        ),
        migrations.RemoveField(
            model_name='messageimage',
            name='message',
        ),
        migrations.RemoveField(
            model_name='messagelink',
            name='message',
        ),
        migrations.RemoveField(
            model_name='messagetext',
            name='message',
        ),
        migrations.RemoveField(
            model_name='messagevideo',
            name='message',
        ),
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.AddField(
            model_name='message',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='messages/audio'),
        ),
        migrations.AddField(
            model_name='message',
            name='delay',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='messages/files'),
        ),
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='messages/images'),
        ),
        migrations.AddField(
            model_name='message',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='map',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=7, max_digits=11), blank=True, null=True, size=2),
        ),
        migrations.AddField(
            model_name='message',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='messages/videos'),
        ),
        migrations.RemoveField(
            model_name='message',
            name='send_datetime',
        ),
        migrations.AlterUniqueTogether(
            name='message',
            unique_together={('order', 'chain')},
        ),
        migrations.DeleteModel(
            name='MessageAudio',
        ),
        migrations.DeleteModel(
            name='MessageButton',
        ),
        migrations.DeleteModel(
            name='MessageDelay',
        ),
        migrations.DeleteModel(
            name='MessageFile',
        ),
        migrations.DeleteModel(
            name='MessageImage',
        ),
        migrations.DeleteModel(
            name='MessageLink',
        ),
        migrations.DeleteModel(
            name='MessageText',
        ),
        migrations.DeleteModel(
            name='MessageVideo',
        ),
    ]
