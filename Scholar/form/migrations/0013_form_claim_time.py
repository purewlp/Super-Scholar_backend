# Generated by Django 4.0.4 on 2022-11-27 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0012_form_institution_form_real_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='claim_time',
            field=models.DateTimeField(null=True),
        ),
    ]