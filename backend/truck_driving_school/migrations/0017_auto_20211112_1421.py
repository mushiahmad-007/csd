# Generated by Django 2.2.24 on 2021-11-12 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('safe_driver', '0068_auto_20211020_2046'),
        ('truck_driving_school', '0016_auto_20211008_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainginRecordDayComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveIntegerField(default=1, verbose_name='Day')),
                ('body', models.TextField(verbose_name='Body')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_training_record_day_comments', to='safe_driver.StudentTest')),
            ],
            options={
                'verbose_name': 'Driver Training Record Day Comment',
                'verbose_name_plural': 'Driver Training Record Day Comments',
                'ordering': ('day',),
            },
        ),
        migrations.AddConstraint(
            model_name='trainginrecorddaycomment',
            constraint=models.UniqueConstraint(fields=('test', 'day'), name='training_record_comment_unique_by_day'),
        ),
    ]