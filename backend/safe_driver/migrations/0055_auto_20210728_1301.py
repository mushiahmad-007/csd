# Generated by Django 2.2.19 on 2021-07-28 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('safe_driver', '0054_auto_20210710_2246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructionbtwbus',
            options={'ordering': ('field_name',), 'verbose_name': 'Instruction for BTW BUS', 'verbose_name_plural': 'Instructions for BTW Class P'},
        ),
        migrations.AlterModelOptions(
            name='instructionpretripbus',
            options={'ordering': ('field_name',), 'verbose_name': 'Instruction for PreTrip BUS', 'verbose_name_plural': 'Instructions for PreTrip Class P'},
        ),
    ]
