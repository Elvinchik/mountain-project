# Generated by Django 3.2.7 on 2021-10-04 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('borabora', '0003_rename_timestam_comment_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='timestamp',
            new_name='timestam',
        ),
    ]