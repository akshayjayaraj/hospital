# Generated by Django 4.0.3 on 2022-03-17 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosapp', '0002_doctors_tb_rename_doctor_patient_tb_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctors_tb',
        ),
        migrations.DeleteModel(
            name='patient_tb',
        ),
    ]
