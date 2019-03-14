# Generated by Django 2.1.5 on 2019-01-29 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoWebinar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=4095, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('active_chats', models.CharField(blank=True, max_length=255, null=True, verbose_name='Active Chats')),
                ('date_activate', models.DateTimeField(blank=True, null=True, verbose_name='Activate date')),
                ('user_counter', models.CharField(blank=True, choices=[('fake', 'fake'), ('real', 'real')], max_length=4, null=True, verbose_name='User counter type')),
                ('min_fake_user_count', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Minimum value for fake people count')),
                ('max_fake_user_count', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Maximum value for fake people count')),
                ('cover_type', models.CharField(blank=True, choices=[('video', 'video'), ('image', 'image')], max_length=5, null=True, verbose_name='Cover before video')),
                ('video_cover', models.FileField(blank=True, null=True, upload_to='projects/webinar/video_cover/', verbose_name='Webinar video cover')),
                ('image_cover', models.ImageField(blank=True, null=True, upload_to='projects/webinar/image_cover/', verbose_name='Webinar image cover')),
            ],
            options={
                'verbose_name': 'Auto Webinar',
                'verbose_name_plural': 'Auto Webinars',
            },
        ),
        migrations.CreateModel(
            name='AutoWebinarFakeChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=63, null=True, verbose_name='Fake name')),
                ('nickname', models.CharField(blank=True, max_length=9, null=True, verbose_name='Fake nickname')),
                ('message', models.TextField(blank=True, max_length=4095, null=True)),
                ('display_time', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('auto_webinar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.AutoWebinar', verbose_name='Auto webinar')),
            ],
            options={
                'verbose_name': 'Fake message',
                'verbose_name_plural': 'Fake messages',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Project name')),
                ('description', models.TextField(blank=True, max_length=4095, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('cover_time', models.PositiveIntegerField(blank=True, null=True, verbose_name='Cover time before video starts (in seconds)')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Webinar',
            fields=[
                ('slug', models.SlugField(max_length=16, primary_key=True, serialize=False, verbose_name='Slug')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=4095, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('active_chats', models.CharField(blank=True, max_length=255, null=True, verbose_name='Active Chats')),
                ('date_activate', models.DateTimeField(blank=True, null=True, verbose_name='Activate date')),
                ('user_counter', models.CharField(blank=True, choices=[('fake', 'fake'), ('real', 'real')], max_length=4, null=True, verbose_name='User counter type')),
                ('min_fake_user_count', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Minimum value for fake people count')),
                ('max_fake_user_count', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Maximum value for fake people count')),
                ('cover_type', models.CharField(blank=True, choices=[('video', 'video'), ('image', 'image')], max_length=5, null=True, verbose_name='Cover before video')),
                ('video_cover', models.FileField(blank=True, null=True, upload_to='projects/webinar/video_cover/', verbose_name='Webinar video cover')),
                ('image_cover', models.ImageField(blank=True, null=True, upload_to='projects/webinar/image_cover/', verbose_name='Webinar image cover')),
                ('video', models.FileField(blank=True, null=True, upload_to='projects/webinar/video/', verbose_name='Webinar video')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
            options={
                'verbose_name': 'Webinar',
                'verbose_name_plural': 'Webinars',
            },
        ),
        migrations.CreateModel(
            name='WebinarFakeChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=63, null=True, verbose_name='Fake name')),
                ('nickname', models.CharField(blank=True, max_length=9, null=True, verbose_name='Fake nickname')),
                ('message', models.TextField(blank=True, max_length=4095, null=True)),
                ('display_time', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('webinar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Webinar', verbose_name='Webinar')),
            ],
            options={
                'verbose_name': 'Fake message',
                'verbose_name_plural': 'Fake messages',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='autowebinar',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]
