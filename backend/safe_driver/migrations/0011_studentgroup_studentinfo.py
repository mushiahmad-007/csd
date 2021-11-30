# Generated by Django 2.2.17 on 2021-03-04 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('safe_driver', '0010_delete_studentinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Student Group',
                'verbose_name_plural': 'Student Group',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Cell')),
                ('city', models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='City')),
                ('country', models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='Country')),
                ('state', models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='State')),
                ('territory', models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='Territory')),
                ('address1', models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='Address 1')),
                ('address2', models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='Address 2')),
                ('zip_code', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='ZIP Code')),
                ('contact_name', models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='Contact Name')),
                ('current_user_identity', models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='Current User Idenity')),
                ('driver_id', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='Driver ID')),
                ('driver_license_number', models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='Driver License Num')),
                ('driver_license_state', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Driver License State')),
                ('driver_license_expire_date', models.DateField(blank=True, default=None, null=True, verbose_name='Dirver License Expiration Date')),
                ('driver_eld_exempt', models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='Driver ELD Exempt')),
                ('endorsements', models.BooleanField(default=False, verbose_name='Endorsement')),
                ('driver_license_class', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default=None, max_length=1, null=True, verbose_name='Driver License Class')),
                ('location', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='Location')),
                ('corrective_lense_required', models.BooleanField(default=False, verbose_name='Corrective Lense Required')),
                ('dot_expiration_date', models.DateField(blank=True, default=None, null=True, verbose_name='DOT Expiration Date')),
                ('driver_duty_status', models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='Driver Duty Status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_info', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student Info',
                'verbose_name_plural': 'Students Info',
                'ordering': ('user__username',),
            },
        ),
    ]