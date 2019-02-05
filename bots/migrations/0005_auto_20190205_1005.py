# Generated by Django 2.1.5 on 2019-02-05 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190131_1242'),
        ('bots', '0004_botmessages_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('interval', models.PositiveIntegerField(verbose_name='interval (hours)')),
            ],
            options={
                'verbose_name': 'Bot Message',
                'verbose_name_plural': 'Bot Messages',
            },
        ),
        migrations.CreateModel(
            name='FacebookBot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('token', models.CharField(max_length=256)),
                ('active', models.BooleanField(default=True)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
            options={
                'verbose_name': 'Facebook Bot',
                'verbose_name_plural': 'Facebook Bots',
            },
        ),
        migrations.CreateModel(
            name='MessagesChain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('start_time', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
            options={
                'verbose_name': 'Messages Chain',
                'verbose_name_plural': 'Messages Chains',
            },
        ),
        migrations.RemoveField(
            model_name='botmessages',
            name='project',
        ),
        migrations.AddField(
            model_name='telegrambot',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='BotMessages',
        ),
        migrations.AddField(
            model_name='botmessage',
            name='chain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bots.MessagesChain'),
        ),
    ]