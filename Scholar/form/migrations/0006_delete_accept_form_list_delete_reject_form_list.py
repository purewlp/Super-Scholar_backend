# Generated by Django 4.0.4 on 2022-11-03 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_accept_form_list_handling_form_list_reject_form_list'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Accept_Form_list',
        ),
        migrations.DeleteModel(
            name='Reject_Form_list',
        ),
    ]