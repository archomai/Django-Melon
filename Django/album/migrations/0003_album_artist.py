# Generated by Django 2.0.2 on 2018-02-07 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0003_auto_20180206_0802'),
        ('album', '0002_remove_album_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ManyToManyField(to='artist.Artist'),
        ),
    ]
