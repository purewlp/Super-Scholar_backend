# Generated by Django 4.0.4 on 2022-11-27 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_user_unread_message_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='real_name',
            field=models.CharField(db_index=True, default='', max_length=200, null=True, verbose_name='对应的作者真名'),
        ),
    ]