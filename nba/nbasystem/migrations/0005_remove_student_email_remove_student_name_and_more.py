# Generated by Django 4.0.4 on 2022-05-18 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nbasystem', '0004_rename_pid_faculty_fid_remove_faculty_sid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sid',
        ),
    ]