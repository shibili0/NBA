# Generated by Django 4.0.4 on 2022-05-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbasystem', '0006_student_email_student_fname_student_lname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='fid',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='name',
            new_name='lname',
        ),
        migrations.RenameField(
            model_name='parent',
            old_name='name',
            new_name='lname',
        ),
        migrations.RenameField(
            model_name='parent',
            old_name='pid',
            new_name='username',
        ),
        migrations.AddField(
            model_name='faculty',
            name='usernane',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='parent',
            name='fname',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
