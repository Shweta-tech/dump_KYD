# Generated by Django 3.0.3 on 2020-04-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyd_dashboard', '0018_auto_20200416_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='F8PwAwc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('project_n', models.CharField(blank=True, max_length=25, null=True)),
                ('beat_n', models.CharField(blank=True, max_length=50, null=True)),
                ('awc_with_code', models.CharField(blank=True, max_length=100, null=True)),
                ('no_anemic_wmn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_pregnant_women', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_tenatus_cmpltd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_rstg_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_etg_xtr_ml_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_trmstr_3wmn_cnsld_imdtbf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_1_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_4_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_anwmic_wmn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_tenatus_cmpltd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_1_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_4_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_etg_xtr_ml_drng_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_rstg_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_trmstr_3wmn_cnsld_imdtbf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f8_pw_awc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='F8PwBeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('project_n', models.CharField(blank=True, max_length=25, null=True)),
                ('beat_n', models.CharField(blank=True, max_length=50, null=True)),
                ('no_anemic_wmn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_pregnant_women', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_tenatus_cmpltd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_rstg_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_etg_xtr_ml_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_trmstr_3wmn_cnsld_imdtbf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_1_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_4_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_anwmic_wmn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_tenatus_cmpltd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_1_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_4_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_etg_xtr_ml_drng_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_rstg_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_trmstr_3wmn_cnsld_imdtbf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f8_pw_beat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='F8PwBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('no_anemic_wmn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_pregnant_women', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_tenatus_cmpltd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_rstg_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_etg_xtr_ml_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_trmstr_3wmn_cnsld_imdtbf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_1_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_4_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_anwmic_wmn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_tenatus_cmpltd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_1_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_4_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_etg_xtr_ml_drng_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_rstg_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_trmstr_3wmn_cnsld_imdtbf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f8_pw_block',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='F8PwProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('project_n', models.CharField(blank=True, max_length=25, null=True)),
                ('no_anemic_wmn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_pregnant_women', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_tenatus_cmpltd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_rstg_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_etg_xtr_ml_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_trmstr_3wmn_cnsld_imdtbf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_1_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_wmn_4_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_anwmic_wmn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_tenatus_cmpltd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_1_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_4_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_etg_xtr_ml_drng_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_rstg_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_trmstr_3wmn_cnsld_imdtbf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f8_pw_project',
                'managed': False,
            },
        ),
    ]
