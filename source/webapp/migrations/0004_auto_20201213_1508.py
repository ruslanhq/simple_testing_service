# Generated by Django 3.1.4 on 2020-12-13 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_choice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AddField(
            model_name='answer',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
