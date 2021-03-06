# Generated by Django 3.0.3 on 2020-04-04 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyd_dashboard', '0005_f51_f9lcblk'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsoChildNdj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('month_n', models.CharField(blank=True, max_length=10, null=True)),
                ('state_n', models.CharField(blank=True, max_length=25, null=True)),
                ('district_n', models.CharField(blank=True, max_length=25, null=True)),
                ('block_n', models.CharField(blank=True, max_length=25, null=True)),
                ('project_n', models.CharField(blank=True, max_length=25, null=True)),
                ('supervisor', models.CharField(blank=True, max_length=100, null=True)),
                ('beat_n', models.CharField(blank=True, max_length=50, null=True)),
                ('awc_with_code', models.CharField(blank=True, max_length=100, null=True)),
                ('aww_ph_no', models.CharField(blank=True, max_length=50, null=True)),
                ('total_no_chld_wgd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('total_no_chld_elgb_wgd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('total_no_chld_ht_was_msrd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('total_no_chld_elgb_hght', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('total_no_unweighed_05yr', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_svrly_uw_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_mdrtly_uw_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_wid_nrmlwt_age', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_svr_wasting', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('total_no_chld_ht_wt_msrd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_mdrtly_wasted_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_wd_nrmlwt_fr_ht', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_svrly_stunted_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('total_no_chld_ht_msrd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_mdrtly_stunted_chld', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_wid_nrmlht_age', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_nwborns_wid_lbw', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('total_no_chld_born_wgd_in_mnth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_of_chld_cmpltd_1yr_immunzt', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('total_no_chld_fr_ag_grtr_12mnths', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_bf_at_birth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('total_no_chld_enrld_cas_born_lstmnth', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_excly_bf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('total_no_chld_0t6mnths_enrld_cas', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_intd_cf_past30d', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('total_no_chld_6t8mnths_enrld_cas', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_appr_cf', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_rcvg_cf_wid_adq_dt_dvsty', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('total_no_chld_6mto2yr_enrld_cas', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_cf_wid_adq_dt_qnty', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('total_no_chld_cf_wid_appr_hndwhg_bfr_fdg', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('no_chld_6t24mnths_enrld_cas', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'conso_child_ndj',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='F1',
        ),
        migrations.DeleteModel(
            name='F2',
        ),
        migrations.DeleteModel(
            name='F3',
        ),
        migrations.DeleteModel(
            name='F4',
        ),
        migrations.DeleteModel(
            name='F51',
        ),
        migrations.DeleteModel(
            name='F6MapBeat',
        ),
        migrations.DeleteModel(
            name='F6MapBlock',
        ),
        migrations.DeleteModel(
            name='F6MapProject',
        ),
        migrations.DeleteModel(
            name='F7IycfAw',
        ),
        migrations.DeleteModel(
            name='F7IycfBlk',
        ),
        migrations.DeleteModel(
            name='F7IycfBt',
        ),
        migrations.DeleteModel(
            name='F7IycfPrjt',
        ),
        migrations.DeleteModel(
            name='F8PwAw',
        ),
        migrations.DeleteModel(
            name='F8PwBlk',
        ),
        migrations.DeleteModel(
            name='F8PwBt',
        ),
        migrations.DeleteModel(
            name='F8PwPrjt',
        ),
        migrations.DeleteModel(
            name='F9LcBlk',
        ),
    ]
