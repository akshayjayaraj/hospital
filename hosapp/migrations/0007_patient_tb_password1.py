# Generated by Django 4.0.3 on 2022-03-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosapp', '0006_doctors_tb_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_tb',
            name='password1',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
