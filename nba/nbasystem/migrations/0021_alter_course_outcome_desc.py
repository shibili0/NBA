# Generated by Django 4.0.4 on 2022-05-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbasystem', '0020_remove_course_outcome_cg_lvl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_outcome',
            name='desc',
            field=models.TextField(),
        ),
    ]
