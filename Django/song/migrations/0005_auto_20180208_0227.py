# Generated by Django 2.0.2 on 2018-02-08 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0004_auto_20180207_0546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(blank=True, max_length=100, verbose_name='장르'),
        ),
        migrations.AddField(
            model_name='song',
            name='lylics',
            field=models.TextField(blank=True, verbose_name='가사'),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=255, verbose_name='곡 제목'),
        ),
    ]
