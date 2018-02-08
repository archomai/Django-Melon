# Generated by Django 2.0.2 on 2018-02-07 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0003_artistsong'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistsong',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='artistsong',
            name='song',
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(related_name='song', to='artist.Artist'),
        ),
        migrations.DeleteModel(
            name='ArtistSong',
        ),
    ]