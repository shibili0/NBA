# Generated by Django 4.0.4 on 2022-05-19 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nbasystem', '0011_co_po_pso'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CO',
            new_name='Course_Outcome',
        ),
        migrations.RenameModel(
            old_name='PO',
            new_name='Program_Outcome',
        ),
        migrations.RenameModel(
            old_name='PSO',
            new_name='Program_Specific_Outcome',
        ),
    ]
