from django.db import models

# Create your models here.
class ConsoChildNdj(models.Model):
    year = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    month_n = models.CharField(max_length=10, blank=True, null=True)
    state_n = models.CharField(max_length=25, blank=True, null=True)
    district_n = models.CharField(max_length=25, blank=True, null=True)
    block_n = models.CharField(max_length=25, blank=True, null=True)
    project_n = models.CharField(max_length=25, blank=True, null=True)
    supervisor = models.CharField(max_length=100, blank=True, null=True)
    beat_n = models.CharField(max_length=50, blank=True, null=True)
    awc_with_code = models.CharField(max_length=100, blank=True, null=True)
    aww_ph_no = models.CharField(max_length=50, blank=True, null=True)
    total_no_chld_wgd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_elgb_wgd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_ht_was_msrd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_elgb_hght = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_unweighed_05yr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_svrly_uw_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_mdrtly_uw_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_wid_nrmlwt_age = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_svr_wasting = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_ht_wt_msrd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_mdrtly_wasted_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_wd_nrmlwt_fr_ht = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_svrly_stunted_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_ht_msrd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_mdrtly_stunted_chld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_wid_nrmlht_age = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_nwborns_wid_lbw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_born_wgd_in_mnth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_of_chld_cmpltd_1yr_immunzt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_fr_ag_grtr_12mnths = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_bf_at_birth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_enrld_cas_born_lstmnth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_excly_bf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_0t6mnths_enrld_cas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_intd_cf_past30d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_6t8mnths_enrld_cas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_appr_cf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_rcvg_cf_wid_adq_dt_dvsty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_6mto2yr_enrld_cas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_cf_wid_adq_dt_qnty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_no_chld_cf_wid_appr_hndwhg_bfr_fdg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_chld_6t24mnths_enrld_cas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conso_child_ndj'


class DistrictPwd(models.Model):
    district_n = models.TextField()

    class Meta:
        managed = False
        db_table = 'district_pwd'