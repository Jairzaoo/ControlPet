# Generated by Django 5.1.1 on 2024-10-12 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPetApp', '0003_alter_pet_vaccine'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='consultation_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]