# Generated by Django 2.2.19 on 2021-04-08 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_driver', '0031_injuryprobabilityvalueswp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vrtuncoupling',
            name='test',
        ),
        migrations.AddField(
            model_name='vrtuncoupling',
            name='verify_firm_to_ground',
            field=models.IntegerField(choices=[(0, 'N/A'), (1, 'Imp'), (2, 'Ok')], default=1, verbose_name='Verify Firm to Ground'),
        ),
        migrations.AlterField(
            model_name='injuryprobabilityvalueswp',
            name='key',
            field=models.CharField(choices=[('animal_bite', 'Animal Bite'), ('amputation', 'Amputation'), ('blunt_force_trauma', 'Blunt Force Trauma'), ('burn', 'Burn'), ('cut', 'Cut'), ('dehydration', 'Denydration'), ('fracture', 'Fracture'), ('frost_bite', 'Frost Bite'), ('heat_stress', 'Heat Stress'), ('sprain', 'Sprain'), ('spider_bite_sting', 'Spider Bite/Sting'), ('strain', 'Strain'), ('stress', 'Stess'), ('toxic_exposure', 'Toxic Exposure')], default=None, help_text='Type key name underscore and without any space', max_length=32, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='vrtcoupling',
            name='back_under_slowly',
            field=models.IntegerField(choices=[(0, 'N/A'), (1, 'Imp'), (2, 'Ok')], default=1, verbose_name='Back Under Slowly'),
        ),
        migrations.AlterField(
            model_name='vrtcoupling',
            name='check_for_hazards',
            field=models.IntegerField(choices=[(0, 'N/A'), (1, 'Imp'), (2, 'Ok')], default=1, verbose_name='Check for Hazards'),
        ),
        migrations.AlterField(
            model_name='vrtcoupling',
            name='secures_equip_properly',
            field=models.IntegerField(choices=[(0, 'N/A'), (1, 'Imp'), (2, 'Ok')], default=1, verbose_name='Secures Equip Properly'),
        ),
        migrations.AlterField(
            model_name='vrtcoupling',
            name='test_tug',
            field=models.IntegerField(choices=[(0, 'N/A'), (1, 'Imp'), (2, 'Ok')], default=1, verbose_name='Test Tug'),
        ),
        migrations.AlterField(
            model_name='vrtcoupling',
            name='verfiy_couple_secure',
            field=models.IntegerField(choices=[(0, 'N/A'), (1, 'Imp'), (2, 'Ok')], default=1, verbose_name='Verify Couple Secure'),
        ),
        migrations.AlterField(
            model_name='vrtuncoupling',
            name='air_lanes_or_light_cord',
            field=models.IntegerField(choices=[(0, 'N/A'), (1, 'Imp'), (2, 'Ok')], default=1, verbose_name='Air Lines/Light Cord'),
        ),
        migrations.AlterField(
            model_name='vrtuncoupling',
            name='chock_wheels',
            field=models.IntegerField(choices=[(0, 'N/A'), (1, 'Imp'), (2, 'Ok')], default=1, verbose_name='Chock Wheels'),
        ),
        migrations.AlterField(
            model_name='vrtuncoupling',
            name='lower_landing_gear',
            field=models.IntegerField(choices=[(0, 'N/A'), (1, 'Imp'), (2, 'Ok')], default=1, verbose_name='Lower Landing Gear'),
        ),
        migrations.AlterField(
            model_name='vrtuncoupling',
            name='lower_trailer_gently',
            field=models.IntegerField(choices=[(0, 'N/A'), (1, 'Imp'), (2, 'Ok')], default=1, verbose_name='Lower trailer Gently'),
        ),
        migrations.AlterField(
            model_name='vrtuncoupling',
            name='secure_equip_properly',
            field=models.IntegerField(choices=[(0, 'N/A'), (1, 'Imp'), (2, 'Ok')], default=1, verbose_name='Secure Equip Properly'),
        ),
        migrations.AlterField(
            model_name='vrtuncoupling',
            name='unlock_fifth_gear',
            field=models.IntegerField(choices=[(0, 'N/A'), (1, 'Imp'), (2, 'Ok')], default=1, verbose_name='Unlock 5th Wheel'),
        ),
    ]
