# Generated by Django 3.0.3 on 2020-07-06 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyd_dashboard', '0030_districtvillagewisegeojson'),
    ]

    operations = [
        migrations.CreateModel(
            name='F10AwcInfra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=20, null=True)),
                ('block_n', models.CharField(blank=True, max_length=20, null=True)),
                ('drinking_water', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('functional_toilet', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('medicine_kit', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('weighing_scale_for_infants', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('weighing_scale_for_mother_and_child', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('infantometer', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('stadiometer', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
            ],
            options={
                'db_table': 'f10_awc_infra',
                'managed': False,
            },
        ),
    ]
