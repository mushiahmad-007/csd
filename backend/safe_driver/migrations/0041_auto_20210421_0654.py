# Generated by Django 2.2.19 on 2021-04-21 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_driver', '0040_auto_20210421_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accidentprobabilityvaluebtwbus',
            name='db_table',
            field=models.CharField(default=None, max_length=250, verbose_name='DB Table'),
        ),
        migrations.AlterField(
            model_name='accidentprobabilityvaluebtwclassa',
            name='db_table',
            field=models.CharField(default=None, max_length=250, verbose_name='DB Table'),
        ),
        migrations.AlterField(
            model_name='accidentprobabilityvaluebtwclassb',
            name='db_table',
            field=models.CharField(default=None, max_length=250, verbose_name='DB Table'),
        ),
        migrations.AlterField(
            model_name='accidentprobabilityvaluebtwclassc',
            name='db_table',
            field=models.CharField(default=None, max_length=250, verbose_name='DB Table'),
        ),
        migrations.AlterField(
            model_name='accidentprobabilityvaluepretripbus',
            name='db_table',
            field=models.CharField(default=None, max_length=250, verbose_name='DB Table'),
        ),
        migrations.AlterField(
            model_name='accidentprobabilityvaluepretripclassa',
            name='db_table',
            field=models.CharField(default=None, max_length=250, verbose_name='DB Table'),
        ),
        migrations.AlterField(
            model_name='accidentprobabilityvaluepretripclassb',
            name='db_table',
            field=models.CharField(default=None, max_length=250, verbose_name='DB Table'),
        ),
        migrations.AlterField(
            model_name='accidentprobabilityvaluepretripclassc',
            name='db_table',
            field=models.CharField(default=None, max_length=250, verbose_name='DB Table'),
        ),
    ]