# Generated by Django 2.1.5 on 2019-03-14 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20190314_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webinaronlinewatcherscount',
            name='fake_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
