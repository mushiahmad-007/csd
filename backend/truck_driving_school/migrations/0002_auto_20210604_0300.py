# Generated by Django 2.2.19 on 2021-06-03 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truck_driving_school', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='defensivedriverknowledgequiz',
            options={'ordering': ('-created',), 'verbose_name': 'Defensive Driver Knowledge Quiz', 'verbose_name_plural': 'Defensive Driver Knowledge Quiz'},
        ),
    ]
