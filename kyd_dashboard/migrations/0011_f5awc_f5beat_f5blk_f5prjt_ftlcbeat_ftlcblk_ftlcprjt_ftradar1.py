# Generated by Django 3.0.3 on 2020-04-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyd_dashboard', '0010_f3'),
    ]

    operations = [
        migrations.CreateModel(
            name='F5Awc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('project_n', models.CharField(blank=True, max_length=25, null=True)),
                ('beat_n', models.CharField(blank=True, max_length=50, null=True)),
                ('awc_with_code', models.CharField(blank=True, max_length=100, null=True)),
                ('nb_lbw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wstd_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stntd_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('uw_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stunting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('low_birth_weight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_bf_at_birth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_excly_bf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_rcvg_cf_wid_adq_dt_dvsty', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_cf_wid_adq_dt_qnty', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('per_no_chld_cf_wid_appr_hndwhg_bfr_fdg', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_intd_cf_p30d', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_child_1yr_immnztn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_intd_cf_6to24mnth_child', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_anwmic_wmn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_4_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_etg_xtr_ml_drng_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_rstg_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_trmstr_3wmn_cnsld_imdtbf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f5_awc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='F5Beat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('project_n', models.CharField(blank=True, max_length=25, null=True)),
                ('beat_n', models.CharField(blank=True, max_length=50, null=True)),
                ('nb_lbw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wstd_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stntd_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('uw_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stunting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('low_birth_weight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_bf_at_birth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_excly_bf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_rcvg_cf_wid_adq_dt_dvsty', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_cf_wid_adq_dt_qnty', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('per_no_chld_cf_wid_appr_hndwhg_bfr_fdg', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_intd_cf_p30d', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_child_1yr_immnztn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_intd_cf_6to24mnth_child', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_anwmic_wmn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_4_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_etg_xtr_ml_drng_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_rstg_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_trmstr_3wmn_cnsld_imdtbf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f5_beat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='F5Blk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('nb_lbw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wstd_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stntd_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('uw_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stunting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('low_birth_weight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_bf_at_birth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_excly_bf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_rcvg_cf_wid_adq_dt_dvsty', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_cf_wid_adq_dt_qnty', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('per_no_chld_cf_wid_appr_hndwhg_bfr_fdg', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_intd_cf_p30d', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_child_1yr_immnztn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_intd_cf_6to24mnth_child', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_anwmic_wmn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_4_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_etg_xtr_ml_drng_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_rstg_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_trmstr_3wmn_cnsld_imdtbf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f5_blk',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='F5Prjt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('project_n', models.CharField(blank=True, max_length=25, null=True)),
                ('nb_lbw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wstd_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stntd_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('uw_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stunting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('low_birth_weight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_bf_at_birth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_excly_bf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_rcvg_cf_wid_adq_dt_dvsty', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_cf_wid_adq_dt_qnty', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('per_no_chld_cf_wid_appr_hndwhg_bfr_fdg', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_chld_intd_cf_p30d', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_child_1yr_immnztn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_intd_cf_6to24mnth_child', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_anwmic_wmn', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_4_anc_vst_dlvry', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_etg_xtr_ml_drng_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_wmn_rstg_drg_prgncy', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('prnt_trmstr_3wmn_cnsld_imdtbf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'f5_prjt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FtLcBeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('project_n', models.CharField(blank=True, max_length=25, null=True)),
                ('beat_n', models.CharField(blank=True, max_length=50, null=True)),
                ('mdrtly_stntd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_stntd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svr_wstg', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('mdrtly_wstd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_uw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('mdrtly_uw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('nb_lbw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stunting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_stunted_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('low_birth_weight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'ft_lc_beat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FtLcBlk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('mdrtly_stntd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_stntd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svr_wstg', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('mdrtly_wstd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_uw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('mdrtly_uw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('nb_lbw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svr_wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stunting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_stunted_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('low_birth_weight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'ft_lc_blk',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FtLcPrjt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('project_n', models.CharField(blank=True, max_length=25, null=True)),
                ('mdrtly_stntd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_stntd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svr_wstg', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('mdrtly_wstd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_uw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('mdrtly_uw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('nb_lbw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svr_wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stunting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_stunted_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('low_birth_weight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'ft_lc_prjt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FtRadar1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('district_n', models.CharField(blank=True, max_length=20, null=True)),
                ('project_n', models.CharField(blank=True, max_length=25, null=True)),
                ('underweight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svr_wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('wasting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('svrly_stunting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('stunting_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('low_birth_weight_percent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'ft_radar1',
                'managed': False,
            },
        ),
    ]