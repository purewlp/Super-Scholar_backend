# Generated by Django 4.0.6 on 2022-10-20 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_alex_id', models.CharField(db_index=True, max_length=50, verbose_name='对应的open_alex_id')),
                ('user_id', models.IntegerField(verbose_name='对应的用户id')),
            ],
            options={
                'db_table': 'scholar_author',
            },
        ),
    ]