# Generated by Django 4.0.6 on 2022-10-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='follow_id',
            field=models.IntegerField(default=0, verbose_name='关注人的id'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='followed_id',
            field=models.IntegerField(default=0, verbose_name='被关注人的id'),
        ),
    ]