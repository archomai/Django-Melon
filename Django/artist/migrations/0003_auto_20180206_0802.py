# Generated by Django 2.0.2 on 2018-02-06 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20180206_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='constellation',
            field=models.CharField(blank=True, max_length=30, verbose_name='별자리'),
        ),
    ]
