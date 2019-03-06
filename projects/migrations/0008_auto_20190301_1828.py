# Generated by Django 2.1.5 on 2019-03-01 18:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20190226_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webinar',
            name='cover_type',
        ),
        migrations.RemoveField(
            model_name='webinar',
            name='date_activate',
        ),
        migrations.AddField(
            model_name='webinar',
            name='stream_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='webinar',
            name='image_cover',
            field=models.ImageField(blank=True, null=True, upload_to='projects/webinar/image_cover', verbose_name='Webinar image cover'),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='projects/webinar/video', verbose_name='Webinar video'),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='video_cover',
            field=models.FileField(blank=True, null=True, upload_to='projects/webinar/video_cover', verbose_name='Webinar video cover'),
        ),
    ]