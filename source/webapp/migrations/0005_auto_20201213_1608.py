# Generated by Django 3.1.4 on 2020-12-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20201213_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='is_completed',
        ),
        migrations.AddField(
            model_name='choice',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]