# Generated by Django 4.1.2 on 2022-11-02 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("follow", "0002_alter_follow_follow_id_alter_follow_followed_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="follow", old_name="follow_id", new_name="user_id",
        ),
        migrations.RemoveField(model_name="follow", name="followed_id",),
        migrations.AddField(
            model_name="follow",
            name="author_id",
            field=models.CharField(default="", max_length=200, verbose_name="被关注人的id"),
        ),
    ]
