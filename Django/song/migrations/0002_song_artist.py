# Generated by Django 2.0.2 on 2018-02-07 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0003_auto_20180206_0802'),
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(to='artist.Artist'),
        ),
    ]
