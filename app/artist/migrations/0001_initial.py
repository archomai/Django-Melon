# Generated by Django 2.0.2 on 2018-02-23 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('melon_id', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='멜론 Artist ID')),
                ('img_profile', models.ImageField(blank=True, upload_to='artist', verbose_name='프로필 이미지')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('real_name', models.CharField(blank=True, max_length=30, verbose_name='본명')),
                ('nationality', models.CharField(blank=True, max_length=50, verbose_name='국적')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='생년월일')),
                ('constellation', models.CharField(blank=True, max_length=30, verbose_name='별자리')),
                ('blood_type', models.CharField(blank=True, choices=[('a', 'A형'), ('b', 'B형'), ('o', 'O형'), ('c', 'AB형'), ('x', '기타')], max_length=1, verbose_name='혈액형')),
                ('intro', models.TextField(blank=True, verbose_name='소개')),
            ],
        ),
    ]
