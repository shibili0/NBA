# Generated by Django 4.0.4 on 2022-05-21 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbasystem', '0024_program_educational_outcome_program_outcome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program_educational_outcome',
            name='peo_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='program_outcome',
            name='po_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='program_specific_outcome',
            name='pso_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
