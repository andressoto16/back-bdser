# Este es un módulo de modelo de Django generado automáticamente.
# Tendrás que hacer lo siguiente manualmente para limpiar esto:
#   * Reorganiza el orden de los modelos
#   * Asegúrate de que cada modelo tenga un campo con primary_key=True
#   * Asegúrate de que cada ForeignKey y OneToOneField tenga `on_delete` configurado con el comportamiento deseado
#   * Elimina las líneas `managed = False` si deseas permitir que Django cree, modifique y elimine la tabla
# Siéntete libre de renombrar los modelos, pero no renombres los valores de db_table ni los nombres de los campos.

from django.db import models

#1
class AReeval(models.Model):                        ## tabla con informacion importante hasta 2020
    ida_reeval = models.BigAutoField(primary_key=True)
    cc = models.CharField(db_column='CC',max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pri_nombre = models.CharField(db_column='PRI_NOMBRE',max_length=1000, blank=True, null=True)  # Field name made lowercase.
    seg_nombre = models.CharField(db_column='SEG_NOMBRE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pri_apellido = models.CharField(db_column='PRI_APELLIDO', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    seg_apellido = models.CharField(db_column='SEG_APELLIDO', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tipo_estudio = models.CharField(db_column='TIPO_ESTUDIO', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    agno_solicita = models.CharField(db_column='AGNO_SOLICITA', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    estado_ot = models.CharField(db_column='ESTADO_OT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ot = models.BigIntegerField(db_column='OT', blank=True, null=True)  # Field name made lowercase.
    motivo_inactiva = models.CharField(db_column='MOTIVO_INACTIVA', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    cerrem_medidas = models.CharField(db_column='CERREM_MEDIDAS', max_length=1000,blank=True, null=True)  # Field name made lowercase.
    cerrem_temporal = models.CharField(db_column='CERREM_TEMPORAL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    gvp_concepto = models.CharField(db_column='GVP_CONCEPTO', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    gvp_recomenda = models.CharField(db_column='GVP_RECOMENDA', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    matriz_actual = models.DecimalField(db_column='MATRIZ_ACTUAL', max_digits=8, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'a_reeval'

#2
class ATempo(models.Model):                     ### tabla sin informacion
    ida_tempo = models.AutoField(db_column='idA_TEMPO', primary_key=True)  # Field name made lowercase.
    cc = models.CharField(db_column='CC', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    nota = models.CharField(db_column='NOTA', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    depto = models.CharField(max_length=1000, blank=True, null=True)
    municipio = models.CharField(max_length=1000, blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'a_tempo'

#3
class AccGruGrupos(models.Model):               ### tabla sin informacion
    acc_gru_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    acc_gru_nombre = models.CharField(max_length=1000, blank=True, null=True)
    acc_gru_desc = models.CharField(max_length=1000, blank=True, null=True)
    acc_gru_nro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_gru_grupos'

#4
class AccMdlModulo(models.Model):               ### tabla sin informacion
    acc_mdl_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    mdl_cod = models.CharField(max_length=1000, db_column='MDL_COD')  # Field name made lowercase.
    mdl_nombre = models.CharField(max_length=1000, db_column='MDL_NOMBRE')  # Field name made lowercase.
    aud_usr_ins = models.CharField(max_length=1000, db_column='AUD_USR_INS', blank=True, null=True)  # Field name made lowercase.
    aud_fch_ins = models.DateTimeField(db_column='AUD_FCH_INS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'acc_mdl_modulo'

#5
class AccParParametro(models.Model):            ### tabla sin informacion
    acc_par_secuancia = models.DecimalField(primary_key=True, max_digits=5, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    mdl_cod = models.CharField(max_length=1000, blank=True, null=True)
    acc_par_intentos = models.DecimalField(max_digits=5, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    acc_par_inactividad = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    acc_par_exp_psswd = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'acc_par_parametro'

#6
class AccParParametros(models.Model):           ### tabla sin informacion
    acc_par_secue = models.DecimalField(db_column='ACC_PAR_SECUE', primary_key=True, max_digits=14, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    acc_par_empresa = models.CharField(max_length=1000, db_column='ACC_PAR_EMPRESA', blank=True, null=True)  # Field name made lowercase.
    acc_par_nit = models.CharField(max_length=1000, db_column='ACC_PAR_NIT', blank=True, null=True)  # Field name made lowercase.
    acc_par_dias = models.DecimalField(db_column='ACC_PAR_DIAS', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'acc_par_parametros'

#7
class AccPerPerfil(models.Model):               ### tabla sin informacion
    acc_per_secue = models.DecimalField(primary_key=True, max_digits=14, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    per_nombre = models.CharField(max_length=1000,db_column='PER_NOMBRE')  # Field name made lowercase.
    per_tab_acc = models.CharField(max_length=1000, db_column='PER_TAB_ACC', blank=True, null=True)  # Field name made lowercase.
    per_sql_acc = models.CharField(max_length=1000, db_column='PER_SQL_ACC', blank=True, null=True)  # Field name made lowercase.
    per_descripcion = models.CharField(max_length=1000, blank=True, null=True)
    per_nroitem = models.DecimalField(max_digits=5, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'acc_per_perfil'

#8
class AccPrgPrograma(models.Model):             ### tabla con información sin importancia
    acc_prg_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    acc_mdl_secue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    prg_cod = models.CharField(max_length=1000, db_column='PRG_COD')  # Field name made lowercase.
    prg_descripcion = models.CharField(max_length=1000, db_column='PRG_DESCRIPCION')  # Field name made lowercase.
    aud_usr_ins = models.CharField(max_length=1000, db_column='AUD_USR_INS', blank=True, null=True)  # Field name made lowercase.
    aud_fch_ins = models.DateTimeField(max_length=1000, db_column='AUD_FCH_INS')  # Field name made lowercase.
    prg_inserta = models.CharField(max_length=1000, db_column='PRG_INSERTA', blank=True, null=True)  # Field name made lowercase.
    prg_modifica = models.CharField(max_length=1000, db_column='PRG_MODIFICA', blank=True, null=True)  # Field name made lowercase.
    prg_elimina = models.CharField(max_length=1000, db_column='PRG_ELIMINA', blank=True, null=True)  # Field name made lowercase.
    prg_consulta = models.CharField(max_length=1000, db_column='PRG_CONSULTA', blank=True, null=True)  # Field name made lowercase.
    acc_gru_secue = models.DecimalField(max_length=1000,max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    prg_url = models.CharField(max_length=1000, blank=True, null=True)
    prg_numitem = models.IntegerField(blank=True, null=True)
    prg_nombre_opcion = models.CharField(max_length=1000, blank=True, null=True)
    prg_action = models.CharField(max_length=1000, blank=True, null=True)
    prg_file_icono = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_prg_programa'

#9
class AccPrivRolUsuar(models.Model):            ### tabla por comfirmar atributos
    acc_priv_codigo = models.CharField(max_length=1000)
    acc_priv_nombre = models.CharField(max_length=1000)
    aud_usr_ins = models.CharField(max_length=1000, blank=True, null=True)
    aud_fch_ins = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_priv_rol_usuar'

#10
class AccProgPerf(models.Model):                ### tabla sin información
    acc_pxp_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    acc_prg_secue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    acc_per_secue = models.DecimalField(max_digits=30, decimal_places=6)
    aud_usr_ins = models.CharField(max_length=1000, db_column='AUD_USR_INS', blank=True, null=True)  # Field name made lowercase.
    aud_fch_ins = models.DateTimeField(db_column='AUD_FCH_INS')  # Field name made lowercase.
    pxp_inserta = models.CharField(max_length=1000, db_column='PXP_INSERTA', blank=True, null=True)  # Field name made lowercase.
    pxp_modifica = models.CharField(max_length=1000, db_column='PXP_MODIFICA', blank=True, null=True)  # Field name made lowercase.
    pxp_elimina = models.CharField(max_length=1000, db_column='PXP_ELIMINA', blank=True, null=True)  # Field name made lowercase.
    pxp_consultar = models.CharField(max_length=1000, db_column='PXP_CONSULTAR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'acc_prog_perf'

#11
class AccPxpProgperf(models.Model):             ### tabla sin información
    acc_pxp_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    acc_prg_secue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    acc_per_secue = models.DecimalField(max_digits=30, decimal_places=6)
    aud_usr_ins = models.CharField(max_length=1000, db_column='AUD_USR_INS', blank=True, null=True)  # Field name made lowercase.
    aud_fch_ins = models.DateTimeField(db_column='AUD_FCH_INS')  # Field name made lowercase.
    pxp_inserta = models.CharField(max_length=1000, db_column='PXP_INSERTA', blank=True, null=True)  # Field name made lowercase.
    pxp_modifica = models.CharField(max_length=1000, db_column='PXP_MODIFICA', blank=True, null=True)  # Field name made lowercase.
    pxp_elimina = models.CharField(max_length=1000, db_column='PXP_ELIMINA', blank=True, null=True)  # Field name made lowercase.
    pxp_consultar = models.CharField(max_length=1000, db_column='PXP_CONSULTAR', blank=True, null=True)  # Field name made lowercase.
    pxp_activo = models.CharField(max_length=1000, db_column='PXP_ACTIVO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'acc_pxp_progperf'

#12
class AccUsuUsuario(models.Model):              ### tabla con información importante
    acc_usu_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    acc_mdl_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    usu_cod = models.CharField(max_length=1000,db_column='USU_COD')  # Field name made lowercase.
    usu_nombre = models.CharField(max_length=1000, db_column='USU_NOMBRE')  # Field name made lowercase.
    acc_per_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    usu_estado = models.CharField(max_length=1000, db_column='USU_ESTADO', blank=True, null=True)  # Field name made lowercase.
    usu_password = models.CharField(max_length=1000, blank=True, null=True)
    acc_usu_mail = models.CharField(max_length=1000, blank=True, null=True)
    acc_usu_celular = models.CharField(max_length=1000, blank=True, null=True)
    tmp_codhos = models.CharField(max_length=1000, blank=True, null=True)
    tmp_nomhos = models.CharField(max_length=1000, blank=True, null=True)
    tmp_tipusu = models.CharField(max_length=1000, blank=True, null=True)
    tmp_medico = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'acc_usu_usuario'


#13                                             ### tabla con información sin importancia
class CerActActos(models.Model):
    cer_act_secue = models.AutoField(primary_key=True)
    cer_act_nom_grupo = models.CharField(max_length=1000, blank=True, null=True)
    cer_act_nom_file = models.CharField(max_length=1000, blank=True, null=True)
    cer_act_nom_path = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_act_actos'

#14
class CerActgGenera(models.Model):              ### tabla con informacion importante
    cer_actg_secue = models.AutoField(primary_key=True)
    usu_cod = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_secue = models.IntegerField(blank=True, null=True)
    cer_actg_fecha = models.DateField(blank=True, null=True)
    cer_actg_hora = models.TimeField(blank=True, null=True)
    cer_actg_nro_acto = models.CharField(max_length=1000, blank=True, null=True)
    cer_actg_fecha_acto = models.DateField(blank=True, null=True)
    cer_actg_nota = models.CharField(max_length=1000, blank=True, null=True)
    cer_actg_origen = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_actg_genera'

#15
class CerActnConfig(models.Model):              ### tabla con información poco importante
    cer_actn_agno = models.IntegerField(primary_key=True)
    cer_actn_nro_acto = models.IntegerField(blank=True, null=True)
    cer_actn_nro_comunicado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_actn_config'

#16
class CerAgeAgenda(models.Model):               ### tabla estática con datos importantes
    cer_age_secue = models.AutoField(primary_key=True)
    cer_age_nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_age_agenda'

#17
class CerBasBaseCerrem(models.Model):          ### tabla con poca información
    cer_bas_secue = models.AutoField(primary_key=True)
    cer_bas_delegado_uno = models.CharField(max_length=1000, blank=True, null=True)
    cer_bas_delegado_dos = models.CharField(max_length=1000, blank=True, null=True)
    cer_bas_delegado_tres = models.CharField(max_length=1000, blank=True, null=True)
    cer_bas_delegado_cuatro = models.CharField(max_length=1000, blank=True, null=True)
    cer_bas_delegado_cinco = models.CharField(max_length=1000, blank=True, null=True)
    cer_bas_voto_uno = models.CharField(max_length=1000, blank=True, null=True)
    cer_bas_voto_dos = models.CharField(max_length=1000, blank=True, null=True)
    cer_bas_voto_tres = models.CharField(max_length=1000, blank=True, null=True)
    cer_bas_voto_cuatro = models.CharField(max_length=1000, blank=True, null=True)
    cer_bas_voto_cinco = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_bas_base_cerrem'

#18
class CerCalCambioCalidad(models.Model):       ### tabla con información importante
    cer_cal_secue = models.AutoField(primary_key=True)
    cer_seg_secue = models.IntegerField(blank=True, null=True)
    usu_cod = models.CharField(max_length=1000, blank=True, null=True)
    cer_cal_fecha = models.DateField(blank=True, null=True)
    cer_cal_hora = models.TimeField(blank=True, null=True)
    cer_cal_observa = models.CharField(max_length=1000, blank=True, null=True)
    cer_cal_temporalidad = models.CharField(max_length=1000, blank=True, null=True)
    cer_cal_recomendaciones = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_cal_cambio_calidad'

#19
class CerCerCerrem(models.Model):             ### tabla con información importante
    cer_cer_secue = models.AutoField(primary_key=True)
    cer_cer_fch_crea = models.DateField(blank=True, null=True)
    cer_cer_agno = models.IntegerField(blank=True, null=True)
    cer_cer_fch_cerrem = models.DateField(blank=True, null=True)
    cer_cer_fch_precerrem = models.DateField(blank=True, null=True)
    cer_par_estado = models.CharField(max_length=1000, blank=True, null=True)
    cer_cer_nota = models.CharField(max_length=1000,blank=True, null=True)
    cer_cer_nro_anual = models.IntegerField(blank=True, null=True)
    cer_cer_tipo = models.CharField(max_length=1000, blank=True, null=True)
    cer_cer_fchacto = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_cer_cerrem'

#20
class CerColColectivo(models.Model):         ### tabla com poca informacion (año 2016)
    cer_col_secue = models.AutoField(primary_key=True)
    cer_col_nombre = models.CharField(max_length=1000, blank=True, null=True)
    cer_col_fch_crea = models.DateField(blank=True, null=True)
    cer_col_acto_origen = models.CharField(max_length=1000,blank=True, null=True)
    cer_col_fch_acto_origen = models.DateField(blank=True, null=True)
    cer_col_estado = models.CharField(max_length=1000,blank=True, null=True)
    cer_col_acto_modifica = models.CharField(max_length=1000, blank=True, null=True)
    cer_col_fch_acto_modifica = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_col_colectivo'

#21
class CerDetMedida(models.Model):            ### tabla con información importante
    cer_det_secue = models.AutoField(primary_key=True)
    cer_med_secue = models.ForeignKey('CerMedMedidas', models.DO_NOTHING, db_column='cer_med_secue', blank=True, null=True)
    cer_eva_secue = models.IntegerField(blank=True, null=True)
    cer_det_cantidad = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cer_det_vlr_calculado = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    cer_med_fecha_inicio = models.DateField(blank=True, null=True)
    cer_par_decision = models.CharField(max_length=1000, blank=True, null=True)
    cer_det_nro_meses = models.IntegerField(blank=True, null=True)
    cer_det_fch_fin = models.DateField(blank=True, null=True)
    cer_seg_secue = models.ForeignKey('CerSegComite', models.DO_NOTHING, db_column='cer_seg_secue', blank=True, null=True)
    cer_par_med_individual = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_det_medida'

#22
class CerDetValoresIndCol(models.Model):       ### tabla con información importante
    idcer_det_valores_ind_col = models.AutoField(primary_key=True)
    cer_col_secue = models.IntegerField(blank=True, null=True)
    cer_cer_secue = models.IntegerField(blank=True, null=True)
    cer_seg2_grupo_poblacional = models.IntegerField(blank=True, null=True)
    cer_seg2_categoria = models.IntegerField(blank=True, null=True)
    cer_det_accion = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg2_nvl_riesgo = models.CharField(max_length=1000, blank=True, null=True)
    cer_med_tipo_medida = models.IntegerField(blank=True, null=True)
    cer_seg_secue = models.IntegerField(blank=True, null=True)
    cer_vlr_calculado_ind_col = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cer_det_cantidad = models.IntegerField(blank=True, null=True)
    cer_det_tipo_ind_col = models.CharField(max_length=1000, blank=True, null=True)
    cer_det_fch_inicio = models.DateField(blank=True, null=True)
    cer_det_meses_agno_actual = models.IntegerField(blank=True, null=True)
    cer_det_meses_agno_sgte = models.IntegerField(blank=True, null=True)
    cer_det_valor_agno_actual = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cer_det_valor_agno_sgte = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_det_valores_ind_col'

#23
class CerDocDoctosOt(models.Model):             ### tabla sin información
    cer_doc_secue = models.AutoField(primary_key=True)
    usu_cod = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_secue = models.IntegerField(blank=True, null=True)
    cer_doc_namefile = models.CharField(max_length=1000, blank=True, null=True)
    cer_par_modulo = models.CharField(max_length=1000, blank=True, null=True)
    cer_par_tipo_docto = models.CharField(max_length=1000, blank=True, null=True)
    cer_doc_nota = models.CharField(max_length=1000, blank=True, null=True)
    cer_doc_fecha = models.DateField(blank=True, null=True)
    cer_doc_hora = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_doc_doctos_ot'

#24
class CerDoceCerrem(models.Model):              ### tabla sin información
    cer_doce_secue = models.AutoField(primary_key=True)
    usu_cod = models.CharField(max_length=1000, blank=True, null=True)
    cer_cer_secue = models.IntegerField(blank=True, null=True)
    cer_doce_namefile = models.CharField(max_length=1000, blank=True, null=True)
    cer_par_tipo_docto = models.CharField(max_length=1000, blank=True, null=True)
    cer_doce_nota = models.CharField(max_length=1000, blank=True, null=True)
    cer_doce_fecha = models.DateField(blank=True, null=True)
    cer_doce_hora = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_doce_cerrem'

#25
class CerEvaEvaluado(models.Model):             ### tabla con información importante
    cer_eva_secue = models.AutoField(primary_key=True)
    cer_eva_identifica = models.CharField(max_length=1000, blank=True, null=True)
    cer_eva_nombre_1 = models.CharField(max_length=1000,blank=True, null=True)
    cer_eva_nombre_2 = models.CharField(max_length=1000, blank=True, null=True)
    cer_eva_apel_1 = models.CharField(max_length=1000, blank=True, null=True)
    cer_eva_apel_2 = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_eva_evaluado'

#26
class CerLogTransaccion(models.Model):          ### tabla de log importante para seguimiento
    cer_log_secue = models.AutoField(primary_key=True)
    cer_seg_secue = models.ForeignKey('CerSegComite', models.DO_NOTHING, db_column='cer_seg_secue', blank=True, null=True)
    usu_cod = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='usu_cod', blank=True, null=True)
    cer_log_fecha = models.DateField(blank=True, null=True)
    cer_log_hora = models.TimeField(blank=True, null=True)
    cer_log_par_actividad = models.CharField(max_length=1000,blank=True, null=True)
    cer_log_observa = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_log_transaccion'

#27
class CerMcolMedida(models.Model):              ### tabla que solo esta guardando valores nulos
    cer_mcol_secue = models.AutoField(primary_key=True)
    cer_par_estado = models.CharField(max_length=1000, blank=True, null=True)
    cer_mcol_fch_registro = models.DateField(blank=True, null=True)
    cer_mcol_fch_inicio = models.DateField(blank=True, null=True)
    cer_col_secue = models.ForeignKey(CerColColectivo, models.DO_NOTHING, db_column='cer_col_secue', blank=True, null=True)
    cer_med_secue = models.ForeignKey('CerMedMedidas', models.DO_NOTHING, db_column='cer_med_secue', blank=True, null=True)
    cer_mcol_vlr_med = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_mcol_medida'

#28
class CerMedMedidas(models.Model):              ### tabla con muy poca información almacenada
    cer_med_secue = models.AutoField(primary_key=True)
    cer_med_nombre = models.CharField(max_length=1000, blank=True, null=True)
    cer_med_descripcion = models.CharField(max_length=1000, blank=True, null=True)
    cer_par_estado = models.CharField(max_length=1000, blank=True, null=True)
    cer_med_codigo = models.CharField(max_length=1000, blank=True, null=True)
    cer_par_tipo_pago = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_med_medidas'

#29
class CerMedcColectivo(models.Model):           ### tabla con solo información del 2016
    cer_medc_secue = models.AutoField(primary_key=True)
    cer_medc_fch_registro = models.DateField(blank=True, null=True)
    cer_par_accion = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_secue = models.IntegerField(blank=True, null=True)
    cer_col_secue = models.ForeignKey(CerColColectivo, models.DO_NOTHING, db_column='cer_col_secue', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_medc_colectivo'

#30
class CerNotNotifica(models.Model):             ### tabla con popca inforemación almacenada
    cer_not_secue = models.AutoField(primary_key=True)
    cer_not_nom_comunica = models.CharField(max_length=1000, blank=True, null=True)
    cer_not_nom_file_notifica = models.CharField(max_length=1000,blank=True, null=True)
    cer_not_nom_path_notifica = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_not_notifica'

#31
class CerSeg2Comite(models.Model):              ### tabla con informacion importante
    cer_seg2_secue = models.AutoField(primary_key=True)
    cer_seg_secue = models.IntegerField(blank=True, null=True)
    cer_seg2_cedula = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg2_nombre1 = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg2_nombre2 = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg2_apellido1 = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg2_apellido2 = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg2_sintesis_hechos = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg2_concepto_gvp = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg2_recomen_gvp = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg2_cargo = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg2_nro_sesion_gvp = models.IntegerField(blank=True, null=True)
    cer_seg2_fch_sesion_gvp = models.DateField(blank=True, null=True)
    cer_seg2_matriz_actual = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    cer_seg2_nivel_riesgo = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg2_grupo_poblacional = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cer_seg2_categoria = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cer_seg2_repar_depto = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cer_seg2_repar_mun = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cer_seg2_repar_dir = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg2_entre_depto = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cer_seg2_entre_mun = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cer_seg2_entre_dir = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg2_matriz_anterior_nota = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg2_tipo_estudio_riesgo = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cer_seg2_ord_grupo_acto = models.IntegerField(blank=True, null=True)
    cer_seg2_matriz_gvp = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    cer_seg2_observa_matriz_gvp = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_seg2_comite'

#32
class CerSegComite(models.Model):               ### tabla con información importante
    cer_seg_secue = models.AutoField(primary_key=True)
    pen_idsolpadreot = models.IntegerField(db_column='pen_idsolpadreOT', blank=True, null=True)  # Field name made lowercase.
    cer_seg_nro_pestana = models.IntegerField(blank=True, null=True)
    cer_seg_nro_general = models.IntegerField(blank=True, null=True)
    cer_seg_recepcion_fch = models.DateField(blank=True, null=True)
    cer_seg_recepcion_hora = models.TimeField(blank=True, null=True)
    usu_cod_recepcion = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='usu_cod_recepcion')
    cer_cer_secue = models.ForeignKey(CerCerCerrem, models.DO_NOTHING, db_column='cer_cer_secue', blank=True, null=True)
    cer_seg_precerrem_fch = models.DateField(blank=True, null=True)
    cer_seg_cerrem_fch = models.DateField(blank=True, null=True)
    cer_seg_observaciones = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_med_sugeridas = models.CharField(max_length=1000, blank=True, null=True)
    cer_par_estado_agendamiento = models.CharField(max_length=1000,blank=True, null=True)
    cer_seg_pre_meses_despues = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cer_par_accion_medida = models.CharField(max_length=1000,blank=True, null=True)
    cer_seg_actoadmin_nro = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_actoadmin_fch = models.DateField(blank=True, null=True)
    cer_seg_acta_nro = models.CharField(max_length=1000,blank=True, null=True)
    cer_seg_acta_fch = models.DateField(blank=True, null=True)
    cer_par_origen_caso = models.CharField(max_length=1000,blank=True, null=True)
    cer_par_acepta_sugerencia = models.CharField(max_length=1000,blank=True, null=True)
    cer_seg_fch_juridica = models.DateField(blank=True, null=True)
    cer_seg_mem_juridica = models.CharField(max_length=1000,blank=True, null=True)
    cer_seg_med_ant_cerrem = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_med_implementa = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_delega_nombre1 = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_delega_nombre2 = models.CharField(max_length=1000,blank=True, null=True)
    cer_seg_delega_nombre3 = models.CharField(max_length=1000,blank=True, null=True)
    cer_seg_delega_nombre4 = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_delega_nombre5 = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_delega_voto1 = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_delega_voto2 = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_delega_voto3 = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_delega_voto4 = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_delega_voto5 = models.CharField(max_length=1000, blank=True, null=True)
    ser_seg_delega_observ1 = models.CharField(max_length=1000,blank=True, null=True)
    ser_seg_delega_observ2 = models.CharField(max_length=1000, blank=True, null=True)
    ser_seg_delega_observ3 = models.CharField(max_length=1000, blank=True, null=True)
    ser_seg_delega_observ4 = models.CharField(max_length=1000, blank=True, null=True)
    ser_seg_delega_observ5 = models.CharField(max_length=1000, blank=True, null=True)
    ser_seg_motivo_agenda = models.CharField(max_length=1000, blank=True, null=True)
    ser_seg_genero_agenda = models.CharField(max_length=1000, blank=True, null=True)
    ser_par_registro_medida = models.CharField(max_length=1000, blank=True, null=True)
    ser_seg_medidas_emerg = models.CharField(max_length=1000, blank=True, null=True)
    ser_seg_matriz_antes = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    cer_seg_tiene_acto = models.CharField(max_length=1000,blank=True, null=True)
    cer_seg_usu_acto = models.CharField(max_length=1000,blank=True, null=True)
    cer_seg_fch_reg_acto = models.DateField(blank=True, null=True)
    cer_seg_nucleo_fliar = models.CharField(max_length=1000,blank=True, null=True)
    cer_seg_dir_notifica = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_nota_adicion = models.CharField(max_length=1000, blank=True, null=True)
    cer_act_secue = models.ForeignKey(CerActActos, models.DO_NOTHING, db_column='cer_act_secue', blank=True, null=True)
    cer_age_secue = models.ForeignKey(CerAgeAgenda, models.DO_NOTHING, db_column='cer_age_secue', blank=True, null=True)
    cer_seg_comunicado = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_def_temporalidad = models.CharField(max_length=1000,blank=True, null=True)
    cer_seg_med_director = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_ok_asesor = models.CharField(max_length=1000,blank=True, null=True)
    cer_seg_obs_asesor = models.CharField(max_length=1000, blank=True, null=True)
    cer_not_secue = models.IntegerField(blank=True, null=True)
    cer_seg_temp_director = models.CharField(max_length=1000,blank=True, null=True)
    cer_seg_med_temporalidad = models.IntegerField(blank=True, null=True)
    cer_seg_devoluc = models.CharField(max_length=1000, blank=True, null=True)
    cer_seg_nro_comunica = models.CharField(max_length=1000,blank=True, null=True)
    cer_seg_fch_comunica = models.DateField(blank=True, null=True)
    cer_seg_comunica_sn = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_seg_comite'

#33
class CerVlrrMedidaAgno(models.Model):          ### tabla con solo información del 2015, 2016, 2017 y 2018
    cer_vlrr_secue = models.AutoField(primary_key=True)
    cer_med_secue = models.IntegerField(blank=True, null=True)
    cer_vlr_agno = models.IntegerField(blank=True, null=True)
    cer_vlr_valor = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cer_vlrr_medida_agno'

#34                                             
class CufAcalAnaCalidad(models.Model):          ### tabla intermedia con informacion sobre reparto
    cuf_acor_secue = models.AutoField(primary_key=True)
    acc_usu_analista = models.ForeignKey(AccUsuUsuario, models.DO_NOTHING, db_column='acc_usu_analista')
    acc_usu_calidad = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='acc_usu_calidad')
    acc_usu_reparto = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'cuf_acal_ana_calidad'

#35
class CufAcorAnaCoordina(models.Model):         ### tabal intermedia entre analista y coordinador
    cuf_acor_secue = models.AutoField(primary_key=True)
    acc_usu_analista = models.ForeignKey(AccUsuUsuario, models.DO_NOTHING, db_column='acc_usu_analista')
    acc_usu_coordina = models.ForeignKey(AccUsuUsuario, models.DO_NOTHING, db_column='acc_usu_coordina', related_name='cufacoranacoordina_acc_usu_coordina_set')

    class Meta:
        managed = False
        db_table = 'cuf_acor_ana_coordina'

#36
class CufActiActividades(models.Model):         ### tabla sin información
    cuf_acti_secue = models.DecimalField(primary_key=True, max_digits=30, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_acti_nombre = models.CharField(max_length=1000, blank=True, null=True)
    cuf_acti_nropaso = models.IntegerField(blank=True, null=True)
    cuf_acti_expresion = models.CharField(max_length=1000, blank=True, null=True)
    cuf_par_tipoactividad = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_acti_estado = models.CharField(max_length=1000,blank=True, null=True)
    cuf_exp_secue = models.ForeignKey('CufExpExpresiones', models.DO_NOTHING, db_column='cuf_exp_secue', blank=True, null=True)
    cuf_proc_secue = models.ForeignKey('CufProcProcesos', models.DO_NOTHING, db_column='cuf_proc_secue', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_acti_actividades'

#37
class CufAcuAcuses(models.Model):               ### tabla con poca información almacenada
    cuf_acu_secue = models.AutoField(primary_key=True)
    cuf_for_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_detc_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_acu_tipo = models.CharField(max_length=1000, blank=True, null=True)
    cuf_acu_estado = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_acu_acuses'

#38
class CufBdData(models.Model):                  ### tabla con información de log de la base de datos(P0_F10_CF)
    cuf_bd_secue = models.AutoField(primary_key=True)
    cuf_sol_secue = models.DecimalField(max_digits=30, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_bd_codigo = models.CharField(max_length=1000, )
    cuf_bd_respuesta = models.CharField(max_length=1000,blank=True, null=True)
    cuf_bd_data = models.CharField(max_length=1000)
    cuf_bd_fil = models.IntegerField()
    cuf_bd_col = models.IntegerField()
    cuf_bd_hoja = models.IntegerField(blank=True, null=True)
    cuf_bd_codingreso = models.CharField(max_length=1000,blank=True, null=True)
    cuf_car_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_gri_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_bd_tipo = models.CharField(max_length=1000,blank=True, null=True)
    cuf_detc_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_bd_datasalida = models.CharField(max_length=1000,blank=True, null=True)
    cuf_bd_grupo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_bd_data'

#39
class CufBloBloqueos(models.Model):             ### tabla con poca información almacenada
    cuf_blo_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_blo_nombre = models.CharField(max_length=1000,blank=True, null=True)
    cuf_blo_descri = models.CharField(max_length=1000,blank=True, null=True)
    cuf_blo_fchini = models.DateTimeField(blank=True, null=True)
    cuf_blo_fchfin = models.DateTimeField(blank=True, null=True)
    cuf_par_estado = models.ForeignKey('CufParParamtos', models.DO_NOTHING, db_column='cuf_par_estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_blo_bloqueos'

#40
class CufCarCargues(models.Model):              ### tabla con información importante con ruta de archivos adjuntos
    cuf_car_secue = models.AutoField(primary_key=True)
    cuf_car_name_origen = models.CharField(max_length=1000)
    cuf_car_name_destino = models.CharField(max_length=1000)
    cuf_sol_secue = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)  # Ajusta decimal_places
    cuf_par_estcargue = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)  # Ajusta decimal_places
    cuf_car_fch_cargue = models.DateField(blank=True, null=True)
    cuf_car_hor_cargue = models.TimeField(blank=True, null=True)
    cuf_car_fch_iniproc = models.DateField(blank=True, null=True)
    cuf_car_hor_iniproc = models.TimeField(blank=True, null=True)
    cuf_car_nro_errores = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)  # Ajusta decimal_places
    cuf_car_ip = models.CharField(max_length=1000, blank=True, null=True)
    cuf_car_tamano = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)  # Ajusta decimal_places
    cuf_car_origen = models.CharField(max_length=1000, blank=True, null=True)
    cuf_car_mail = models.CharField(max_length=1000, blank=True, null=True)
    cuf_car_fch_envio = models.DateField(blank=True, null=True)
    cuf_car_hor_envio = models.TimeField(blank=True, null=True)
    cuf_seg_recibo = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)  # Ajusta decimal_places
    cuf_seg_proceso = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)  # Ajusta decimal_places
    cuf_seg_envio = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)  # Ajusta decimal_places
    cuf_par_tipope = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)  # Ajusta decimal_places
    cuf_car_asunto = models.CharField(max_length=1000, blank=True, null=True)
    cuf_par_estsolicitud = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)  # Ajusta decimal_places
    acc_usu_secue = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)  # Ajusta decimal_places
    cuf_err_secue = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)  # Ajusta decimal_places
    cuf_car_comando = models.CharField(max_length=1000, blank=True, null=True)
    cuf_sol_padre = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)  # Ajusta decimal_places
    cuf_car_proceso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_car_cargues'


#41
class CufCaruCargousu(models.Model):            ### tabla con los cargos de los usuarios
    cuf_caru_secue = models.AutoField(primary_key=True)
    cuf_caru_nombre = models.CharField(max_length=1000,blank=True, null=True)
    cuf_caru_codigo = models.CharField(max_length=1000,blank=True, null=True)
    cuf_caru_estado = models.CharField(max_length=1000,blank=True, null=True)
    acc_usu_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'cuf_caru_cargousu'

#42
class CufColsSalida(models.Model):              ### tabla con información por verificar
    cuf_cols_secue = models.DecimalField(db_column='CUF_COLS_SECUE', primary_key=True, max_digits=30, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_for_secue = models.DecimalField(db_column='CUF_FOR_SECUE', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_detc_secue = models.DecimalField(db_column='CUF_DETC_SECUE', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_cols_pestana = models.CharField(max_length=1000,db_column='CUF_COLS_PESTANA', blank=True, null=True)  # Field name made lowercase.
    cuf_cols_fila = models.IntegerField(blank=True, null=True)
    cuf_cols_col = models.IntegerField(blank=True, null=True)
    cuf_par_tipodato = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_sol_tiposalida = models.IntegerField(blank=True, null=True)
    cuf_sol_origdata = models.IntegerField(blank=True, null=True)
    cuf_sol_columna = models.CharField(max_length=1000,blank=True, null=True)
    cuf_for_fororigen = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_par_procprelle = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'cuf_cols_salida'

#43
class CufConConfigura(models.Model):            ### tabla sin información
    cuf_con_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_con_descri = models.CharField(max_length=1000,blank=True, null=True)
    cuf_con_valor = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_con_configura'

#44
class CufDcarDetalle(models.Model):             ### tabla con valoidaciones para las celdas
    cuf_dcar_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_car_secue = models.ForeignKey(CufCarCargues, models.DO_NOTHING, db_column='cuf_car_secue', blank=True, null=True)
    cuf_dcar_descripcion = models.CharField(max_length=1000,blank=True, null=True)
    cuf_dcar_campo = models.CharField(max_length=1000,blank=True, null=True)
    cuf_dcar_col = models.IntegerField(blank=True, null=True)
    cuf_dcar_fil = models.IntegerField(blank=True, null=True)
    cuf_dcar_valor = models.CharField(max_length=1000,blank=True, null=True)
    cuf_dcar_hoja = models.IntegerField(blank=True, null=True)
    cuf_dcar_pestana = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_dcar_detalle'

#45
class CufDetcColumnas(models.Model):            ### tabla con condicionamientos de las celdas
    cuf_detc_secue = models.DecimalField(primary_key=True, max_digits=30, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_for_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_par_tipval = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_par_tipdat = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_gran_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_detc_nombre = models.CharField(max_length=1000,blank=True, null=True)
    cuf_detc_descri = models.CharField(max_length=1000,blank=True, null=True)
    cuf_detc_columna = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_detc_fila = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_detc_long = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_detc_decimal = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_detc_obliga = models.CharField(max_length=1000,blank=True, null=True)
    cuf_detc_hoja = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_detc_codigo = models.CharField(max_length=1000,blank=True, null=True)
    cuf_par_tipform = models.CharField(max_length=1000,blank=True, null=True)
    cuf_gri_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_detc_namecol = models.CharField(max_length=1000,blank=True, null=True)
    cuf_detc_pestana = models.CharField(max_length=1000,blank=True, null=True)
    cuf_par_idproceso = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'cuf_detc_columnas'

#46
class CufDranDetrangos(models.Model):           ### tabla con condicionamientos de las celdas
    cuf_dran_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_gran_secue = models.ForeignKey('CufGranGrurangos', models.DO_NOTHING, db_column='cuf_gran_secue', blank=True, null=True)
    cuf_dran_nombre = models.CharField(max_length=1000,blank=True, null=True)
    cuf_dran_valor = models.CharField(max_length=1000,blank=True, null=True)
    cuf_dran_estado = models.CharField(max_length=1000,blank=True, null=True)
    cuf_dran_codequi = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_dran_detrangos'

#47
class CufDrasRansec(models.Model):              ### tabla con condicionamientos de las celdas
    cuf_dras_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_gran_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_dran_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_dras_valor = models.CharField(max_length=1000,blank=True, null=True)
    id_secretaria = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'cuf_dras_ransec'

#48
class CufErrErrores(models.Model):              ### tabla para manejo de errores de las celdas
    cuf_err_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_err_nombre = models.CharField(max_length=1000,blank=True, null=True)
    cuf_err_descr = models.CharField(max_length=1000,blank=True, null=True)
    cuf_err_estado = models.CharField(max_length=1000,blank=True, null=True)
    cuf_err_codigo = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_err_errores'

#49
class CufEstadistica(models.Model):             ### tabla para verificar atributos
    cuf_secue = models.DecimalField(unique=True, max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_solicitud = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_codigo = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_respuesta = models.CharField(max_length=1000)
    cuf_ingreso = models.CharField(max_length=1000,blank=True, null=True)
    cuf_fila = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_col = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_hoja = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_codingreso = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_estadistica'

#50
class CufExcErrxcarga(models.Model):            ### tabla sin información
    cuf_exc_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_err_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_sol_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_exc_descr = models.CharField(max_length=1000,blank=True, null=True)
    cuf_exc_fil = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_exc_col = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'cuf_exc_errxcarga'

#51
class CufExpExpresiones(models.Model):          ### tabla sin información
    cuf_exp_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_detc_columna = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_proc_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_par_opecompara = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_par_opelogica = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_exp_estado = models.CharField(max_length=1000,blank=True, null=True)
    cuf_exp_valor = models.CharField(max_length=1000,blank=True, null=True)
    cuf_exp_descri = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_exp_expresiones'

#52
class CufForFormatos(models.Model):             ### tabla con informacion sobre la ruta de los formatos
    cuf_for_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_par_tipfor = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_par_tipper = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_par_tiparc = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_for_nombre = models.CharField(max_length=1000,blank=True, null=True)
    cuf_for_descri = models.CharField(max_length=1000,blank=True, null=True)
    cuf_for_diaini = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_for_nrodias = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_for_path = models.CharField(max_length=1000,blank=True, null=True)
    cuf_for_estado = models.CharField(max_length=1000,blank=True, null=True)
    cuf_for_cabecera = models.CharField(max_length=1000,blank=True, null=True)
    cuf_for_prellena = models.CharField(max_length=1000,blank=True, null=True)
    cuf_for_plantilla = models.CharField(max_length=1000,blank=True, null=True)
    cuf_for_filas = models.IntegerField(blank=True, null=True)
    cuf_for_alias = models.CharField(max_length=1000,blank=True, null=True)
    cuf_par_tipcargue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_for_ambiente = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_for_formatos'

#53
class CufFxsFormxsecre(models.Model):           ### tabla con poca información
    cuf_fxs_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_par_tiparc = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_for_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_fxs_estado = models.CharField(max_length=1000,blank=True, null=True)
    acc_usu_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'cuf_fxs_formxsecre'

#54
class CufGenCatalogo(models.Model):             ### tabla sin información
    cuf_gen_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_for_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_par_estcat = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_gen_fchcrea = models.DateField(blank=True, null=True)
    cuf_gen_fchgen = models.DateField(blank=True, null=True)
    cuf_gen_agno = models.DecimalField(max_digits=6, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'cuf_gen_catalogo'

#55
class CufGranGrurangos(models.Model):           ### atributos de las celdas
    cuf_gran_secue = models.DecimalField(primary_key=True, max_digits=30, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_gran_nombre = models.CharField(max_length=1000,blank=True, null=True)
    cuf_gran_descr = models.CharField(max_length=1000,blank=True, null=True)
    cuf_gran_estado = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_gran_grurangos'

#56
class CufGriGrillas(models.Model):              ### atributos de las celdas
    cuf_gri_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_gri_codigo = models.CharField(max_length=1000,blank=True, null=True)
    cuf_gri_nombre = models.CharField(max_length=1000,blank=True, null=True)
    cuf_gri_descri = models.CharField(max_length=1000,blank=True, null=True)
    cuf_gri_fila = models.IntegerField(blank=True, null=True)
    cuf_gri_maxfila = models.IntegerField(blank=True, null=True)
    cuf_gri_nametabla = models.CharField(max_length=1000,blank=True, null=True)
    cuf_gri_estado = models.CharField(max_length=1000,blank=True, null=True)
    cuf_for_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_par_codtipform = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_gri_altofila = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_gri_grillas'

#57
class CufLog(models.Model):                     ### tabla con log de la base de datos
    cuf_secue = models.AutoField(primary_key=True)
    cuf_id = models.IntegerField(blank=True, null=True)
    cuf_descri = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_log'

#58
class CufLogCargue(models.Model):               ### tabla con log de la base de datos
    cuf_log_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_sol_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_log_fchtx = models.DateField(blank=True, null=True)
    cuf_log_descrip = models.CharField(max_length=1000,blank=True, null=True)
    cuf_par_parpro = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'cuf_log_cargue'

#59
class CufLogeErrores(models.Model):             ### tabla con log de la base de datos
    cuf_loge_secue = models.AutoField(primary_key=True)
    cuf_err_secue = models.IntegerField(blank=True, null=True)
    cuf_loge_descripcion = models.CharField(max_length=1000,blank=True, null=True)
    cuf_loge_clase = models.CharField(max_length=1000,blank=True, null=True)
    cuf_loge_metodo = models.CharField(max_length=1000,blank=True, null=True)
    cuf_loge_mensaje = models.CharField(max_length=1000,blank=True, null=True)
    cuf_loge_tipoerror = models.IntegerField(blank=True, null=True)
    cuf_loge_fecha = models.DateField(blank=True, null=True)
    cuf_loge_hora = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_loge_errores'

#60
class CufMailConfig(models.Model):              ### tabla con los patrones para envio de correo
    cuf_mail_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_mail_descri = models.CharField(max_length=1000,blank=True, null=True)
    cuf_mail_asunto = models.CharField(max_length=1000,blank=True, null=True)
    cuf_mail_texto = models.CharField(max_length=1000,blank=True, null=True)
    cuf_mail_firma = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_mail_config'

#61
class CufOpeOperacion(models.Model):            ### tabla con poca información
    cuf_ope_secue = models.DecimalField(primary_key=True, max_digits=30, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_ope_codigo = models.CharField(max_length=1000,blank=True, null=True)
    cuf_ope_nombre = models.CharField(max_length=1000,blank=True, null=True)
    cuf_ope_descr = models.CharField(max_length=1000,blank=True, null=True)
    cuf_ope_estado = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_ope_operacion'

#62
class CufParParamtos(models.Model):             ### tabla estática con los estados del caso
    cuf_par_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_par_nombre = models.CharField(max_length=1000,blank=True, null=True)
    cuf_par_descr = models.CharField(max_length=1000,blank=True, null=True)
    cuf_par_tipo = models.CharField(max_length=1000,blank=True, null=True)
    cuf_par_estado = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_par_paramtos'

#63
class CufPgePargeneral(models.Model):           ### tabla con un solo dato guardado (1, NUKIBI, 79465403, C:ISAHCARCHIVOS\test)
    cuf_pge_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_pge_razon = models.CharField(max_length=1000,)
    cuf_pge_nit = models.CharField(max_length=1000,)
    cuf_pge_pathrep = models.CharField(max_length=1000,)

    class Meta:
        managed = False
        db_table = 'cuf_pge_pargeneral'

#64
class CufProcProcesos(models.Model):            ### tabla con solo dos datos almacenados 
    cuf_proc_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_proc_nombre = models.CharField(max_length=1000,blank=True, null=True)
    cuf_proc_descri = models.CharField(max_length=1000,blank=True, null=True)
    cuf_par_tipflujo = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_proc_nropaso = models.IntegerField(blank=True, null=True)
    cuf_for_secue = models.ForeignKey(CufForFormatos, models.DO_NOTHING, db_column='cuf_for_secue', blank=True, null=True)
    cuf_proc_estado = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_proc_procesos'

#65
class CufRegCalidad(models.Model):              ###  tabla para el registro de calidad
    cuf_reg_secue = models.AutoField(primary_key=True)
    cuf_reg_fecha = models.DateField()
    cuf_reg_hora = models.TimeField()
    cuf_reg_usuario = models.CharField(max_length=1000)
    cuf_reg_solpadre = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'cuf_reg_calidad'

#66
class CufRegRegional(models.Model):             ### tabla con poca información registrada
    cuf_reg_secue = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_reg_codigo = models.CharField(max_length=1000,blank=True, null=True)
    cuf_reg_nombre = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_reg_regional'

#67
class CufRenfReenvioform(models.Model):         ### tabla con poca informacion registrada
    cuf_renf_secue = models.AutoField(primary_key=True)
    cuf_detc_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_for_origen = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_for_destino = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_renf_estado = models.CharField(max_length=1000,blank=True, null=True)
    cuf_detc_sol_padre = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'cuf_renf_reenvioform'

#68
class CufSegEventos(models.Model):              ### tabla con poca informacion registrada
    cuf_seg_secue = models.DecimalField(primary_key=True, max_digits=30, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_seg_fchreg = models.DateTimeField(blank=True, null=True)
    cuf_seg_dia = models.IntegerField(blank=True, null=True)
    cuf_seg_mes = models.IntegerField(blank=True, null=True)
    cuf_seg_agno = models.IntegerField(blank=True, null=True)
    cuf_seg_hora = models.IntegerField(blank=True, null=True)
    cuf_seg_ip = models.CharField(max_length=1000,blank=True, null=True)
    cuf_ope_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_seg_descri = models.CharField(max_length=1000,blank=True, null=True)
    cuf_seg_mail_destino = models.CharField(max_length=1000,blank=True, null=True)
    cuf_seg_mail_origen = models.CharField(max_length=1000,blank=True, null=True)
    acc_usu_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_seg_nroregistros = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_seg_eventos'

#69                                             ### tabla con la ruta de documentos
class CufSolSolicitud(models.Model):
    cuf_sol_secue = models.AutoField(primary_key=True)
    cuf_par_tiparc = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_for_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_gen_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_par_estsol = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_par_tipper = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    id_secretaria = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_sol_fchini = models.DateField(blank=True, null=True)
    cuf_sol_fchfin = models.DateField(blank=True, null=True)
    cuf_sol_nroper = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_sol_agno = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_sol_fileori = models.CharField(max_length=1000,blank=True, null=True)
    cuf_sol_filesis = models.CharField(max_length=1000,blank=True, null=True)
    cuf_sol_fchcar = models.DateField(blank=True, null=True)
    cuf_sol_maquina = models.CharField(max_length=1000,blank=True, null=True)
    acc_usu_secue = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_sol_fchcertifica = models.DateField(blank=True, null=True)
    cuf_sol_horcertifica = models.TimeField(blank=True, null=True)
    cuf_sol_nrocertifica = models.CharField(max_length=1000,blank=True, null=True)
    cuf_err_secue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_car_secue = models.IntegerField(blank=True, null=True)
    cuf_sol_estgeneral = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_int_sispro = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuf_sol_solicitud'

#70                                     
class CufTipTippar(models.Model):                   ### atributos de las celdas
    cuf_tip_codigo = models.CharField(max_length=1000,primary_key=True)
    cuf_tip_descripcion = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'cuf_tip_tippar'

#71
class DimSecretarias(models.Model):                 ### Metadata de las secretarias regionales
    id_secretaria = models.DecimalField(primary_key=True, max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    id_men = models.CharField(max_length=1000,blank=True, null=True)
    codigo_secretaria = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    secretaria = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_secretarias'

#72                     
class ErrError(models.Model):                       ### tabla que poca información almacenada
    err_cod = models.IntegerField(primary_key=True)
    err_dbms = models.CharField(max_length=1000)
    err_descr = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'err_error'

#73
class IfActCerrem(models.Model):                    ### tabla que poca información almacenada
    if_act_secue = models.AutoField(primary_key=True)
    if_act_sol_padre = models.DecimalField(max_digits=30, decimal_places=6)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_act_fecha = models.DateField()
    if_act_hora = models.TimeField()
    if_act_usu = models.DecimalField(max_digits=30, decimal_places=6)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_act_motivo = models.CharField(max_length=1000)
    if_act_memo = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'if_act_cerrem'

#74
class IfActa(models.Model):                         ### tabla con información importante ac_doev_009 es cedula evaluado
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=30, decimal_places=6)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    ac_ortr_012 = models.DecimalField(db_column='AC_ORTR_012', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ac_diac_001 = models.DecimalField(db_column='AC_DIAC_001', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ac_meac_002 = models.DecimalField(db_column='AC_MEAC_002', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ac_anac_003 = models.CharField(max_length=1000,db_column='AC_ANAC_003', blank=True, null=True)  # Field name made lowercase.
    ac_hoac_004 = models.CharField(max_length=1000,db_column='AC_HOAC_004', blank=True, null=True)  # Field name made lowercase.
    ac_miac_005 = models.CharField(max_length=1000,db_column='AC_MIAC_005', blank=True, null=True)  # Field name made lowercase.
    ac_caac_006 = models.DecimalField(db_column='AC_CAAC_006', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ac_obac_007 = models.CharField(max_length=1000,db_column='AC_OBAC_007', blank=True, null=True)  # Field name made lowercase.
    ac_evac_008 = models.CharField(max_length=1000,db_column='AC_EVAC_008', blank=True, null=True)  # Field name made lowercase.
    ac_nofu_010 = models.CharField(max_length=1000,db_column='AC_NOFU_010', blank=True, null=True)  # Field name made lowercase.
    ac_doev_009 = models.CharField(max_length=1000,db_column='AC_DOEV_009', blank=True, null=True)  # Field name made lowercase.
    ac_dofu_011 = models.CharField(max_length=1000,db_column='AC_DOFU_011', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_acta'

#75
class IfAnuAnulaot(models.Model):                   ### tabla con información importante
    anu_id_secue = models.AutoField(primary_key=True)
    anu_sol_padre = models.DecimalField(max_digits=30, decimal_places=6)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    anu_fecha = models.DateField()
    anu_hora = models.TimeField()
    anu_usu = models.DecimalField(max_digits=30, decimal_places=6)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    anu_tipo_anulacion = models.CharField(max_length=1000)
    anu_descripcion = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'if_anu_anulaot'

#76
class IfCalidad(models.Model):                      ### tabla con información de la operación de calidad
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    ca_ortr_007 = models.DecimalField(db_column='CA_ORTR_007', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_diso_061 = models.DecimalField(db_column='CA_DISO_061', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_meso_062 = models.DecimalField(db_column='CA_MESO_062', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_anso_063 = models.DecimalField(db_column='CA_ANSO_063', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_vari_071 = models.DecimalField(db_column='CA_VARI_071', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_foco_064 = models.DecimalField(db_column='CA_FOCO_064', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_desp_072 = models.DecimalField(db_column='CA_DESP_072', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_conse_065 = models.DecimalField(db_column='CA_CONSE_065', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_acme_073 = models.DecimalField(db_column='CA_ACME_073', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_docu_066 = models.DecimalField(db_column='CA_DOCU_066', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_somp_074 = models.DecimalField(db_column='CA_SOMP_074', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_enev_067 = models.DecimalField(db_column='CA_ENEV_067', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_ense_075 = models.DecimalField(db_column='CA_ENSE_075', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_ente_068 = models.DecimalField(db_column='CA_ENTE_068', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_cuer_076 = models.DecimalField(db_column='CA_CUER_076', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_inen_069 = models.DecimalField(db_column='CA_INEN_069', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_vari_077 = models.DecimalField(db_column='CA_VARI_077', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_anen_070 = models.DecimalField(db_column='CA_ANEN_070', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_diso_080 = models.DecimalField(db_column='CA_DISO_080', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_meso_081 = models.DecimalField(db_column='CA_MESO_081', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_anso_082 = models.DecimalField(db_column='CA_ANSO_082', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_meso_083 = models.CharField(max_length=1000,db_column='CA_MESO_083', blank=True, null=True)  # Field name made lowercase.
    ca_meso_084 = models.CharField(max_length=1000,db_column='CA_MESO_084', blank=True, null=True)  # Field name made lowercase.
    ca_meso_085 = models.CharField(max_length=1000,db_column='CA_MESO_085', blank=True, null=True)  # Field name made lowercase.
    ca_anca_090 = models.CharField(max_length=1000,db_column='CA_ANCA_090', blank=True, null=True)  # Field name made lowercase.
    ca_amca_091 = models.CharField(max_length=1000,db_column='CA_AMCA_091', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_calidad'

#77
class IfCalidadGrilla(models.Model):                ### tabla con información de la operación de calidad
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    ca_cope_086 = models.DecimalField(db_column='CA_COPE_086', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ca_ajan_078 = models.CharField(max_length=1000,db_column='CA_AJAN_078', blank=True, null=True)  # Field name made lowercase.
    ca_obse_079 = models.CharField(max_length=1000,db_column='CA_OBSE_079', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_calidad_grilla'

#78
class IfCierreCalidad(models.Model):                ### tabla sin información
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    if_nroid = models.DecimalField(db_column='IF_NROID', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_nroot = models.DecimalField(db_column='IF_NROOT', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_analista_nombre = models.CharField(max_length=1000,db_column='IF_ANALISTA_NOMBRE', blank=True, null=True)  # Field name made lowercase.
    if_analista_id = models.CharField(max_length=1000,db_column='IF_ANALISTA_ID', blank=True, null=True)  # Field name made lowercase.
    if_estado_general = models.CharField(max_length=1000,db_column='IF_ESTADO_GENERAL', blank=True, null=True)  # Field name made lowercase.
    if_estado_solicitud = models.CharField(max_length=1000,db_column='IF_ESTADO_SOLICITUD', blank=True, null=True)  # Field name made lowercase.
    if_estado_cargue = models.CharField(max_length=1000,db_column='IF_ESTADO_CARGUE', blank=True, null=True)  # Field name made lowercase.
    if_fch_cargue = models.CharField(max_length=1000,db_column='IF_FCH_CARGUE', blank=True, null=True)  # Field name made lowercase.
    if_cierre = models.CharField(max_length=1000,db_column='IF_CIERRE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_cierre_calidad'

#79
class IfConsentimiento(models.Model):               ### datos del consentimiento co-diev-30 es la cedula
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    co_ortr_001 = models.DecimalField(db_column='CO_ORTR_001', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_tiev_011 = models.DecimalField(db_column='CO_TIEV_011', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_niev_012 = models.CharField(max_length=1000,db_column='CO_NIEV_012', blank=True, null=True)  # Field name made lowercase.
    co_pnev_013 = models.CharField(max_length=1000,db_column='CO_PNEV_013', blank=True, null=True)  # Field name made lowercase.
    co_snev_014 = models.CharField(max_length=1000,db_column='CO_SNEV_014', blank=True, null=True)  # Field name made lowercase.
    co_paev_015 = models.CharField(max_length=1000,db_column='CO_PAEV_015', blank=True, null=True)  # Field name made lowercase.
    co_saev_016 = models.CharField(max_length=1000,db_column='CO_SAEV_016', blank=True, null=True)  # Field name made lowercase.
    co_deco_017 = models.DecimalField(db_column='CO_DECO_017', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_muco_018 = models.DecimalField(db_column='CO_MUCO_018', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_dico_019 = models.DecimalField(db_column='CO_DICO_019', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_meco_020 = models.DecimalField(db_column='CO_MECO_020', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_anco_021 = models.DecimalField(db_column='CO_ANCO_021', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_hoco_022 = models.DecimalField(db_column='CO_HOCO_022', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_mico_023 = models.DecimalField(db_column='CO_MICO_023', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_fope_024 = models.DecimalField(db_column='CO_FOPE_024', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_inva_025 = models.DecimalField(db_column='CO_INVA_025', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_coan_026 = models.DecimalField(db_column='CO_COAN_026', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_cope_027 = models.DecimalField(db_column='CO_COPE_027', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_obco_028 = models.CharField(max_length=1000,db_column='CO_OBCO_028', blank=True, null=True)  # Field name made lowercase.
    co_noev_029 = models.CharField(max_length=1000,db_column='CO_NOEV_029', blank=True, null=True)  # Field name made lowercase.
    co_noan_031 = models.CharField(max_length=1000,db_column='CO_NOAN_031', blank=True, null=True)  # Field name made lowercase.
    co_diev_030 = models.CharField(max_length=1000,db_column='CO_DIEV_030', blank=True, null=True)  # Field name made lowercase.
    co_dian_032 = models.CharField(max_length=1000,db_column='CO_DIAN_032', blank=True, null=True)  # Field name made lowercase.
    co_fope_033 = models.DecimalField(db_column='CO_FOPE_033', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_obde_034 = models.CharField(max_length=1000,db_column='CO_OBDE_034', blank=True, null=True)  # Field name made lowercase.
    co_noev_035 = models.CharField(max_length=1000,db_column='CO_NOEV_035', blank=True, null=True)  # Field name made lowercase.
    co_noan_037 = models.CharField(max_length=1000,db_column='CO_NOAN_037', blank=True, null=True)  # Field name made lowercase.
    co_diev_036 = models.CharField(max_length=1000,db_column='CO_DIEV_036', blank=True, null=True)  # Field name made lowercase.
    co_dian_038 = models.CharField(max_length=1000,db_column='CO_DIAN_038', blank=True, null=True)  # Field name made lowercase.
    co_evaluado_mail = models.CharField(max_length=1000,db_column='CO_EVALUADO_MAIL', blank=True, null=True)  # Field name made lowercase.
    co_dir_entre = models.CharField(max_length=1000,db_column='CO_DIR_ENTRE', blank=True, null=True)  # Field name made lowercase.
    co_fch_entre = models.DateField(db_column='CO_FCH_ENTRE', blank=True, null=True)  # Field name made lowercase.
    co_dep_entre = models.DecimalField(db_column='CO_DEP_ENTRE', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_mun_entre = models.DecimalField(db_column='CO_MUN_ENTRE', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'if_consentimiento'

#80
class IfContactos(models.Model):                    ### tabla con información con poco datos importantes
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    co_orta_001 = models.DecimalField(db_column='CO_ORTA_001', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'if_contactos'

#81
class IfContactosGrilla(models.Model):              ### tabla con informacion importante
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    co_inpr_032 = models.DecimalField(db_column='CO_INPR_032', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_dia1_017 = models.DecimalField(db_column='CO_DIA1_017', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_mes1_018 = models.DecimalField(db_column='CO_MES1_018', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_ano1_019 = models.DecimalField(db_column='CO_ANO1_019', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_hoi1_020 = models.DecimalField(db_column='CO_HOI1_020', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_mii1_021 = models.DecimalField(db_column='CO_MII1_021', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_hof1_022 = models.DecimalField(db_column='CO_HOF1_022', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_mif1_023 = models.DecimalField(db_column='CO_MIF1_023', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    co_teo1_024 = models.CharField(max_length=1000,db_column='CO_TEO1_024', blank=True, null=True)  # Field name made lowercase.
    co_ted1_025 = models.CharField(max_length=1000,db_column='CO_TED1_025', blank=True, null=True)  # Field name made lowercase.
    co_rec1_026 = models.CharField(max_length=1000,db_column='CO_REC1_026', blank=True, null=True)  # Field name made lowercase.
    co_ent1_027 = models.CharField(max_length=1000,db_column='CO_ENT1_027', blank=True, null=True)  # Field name made lowercase.
    co_car1_028 = models.CharField(max_length=1000,db_column='CO_CAR1_028', blank=True, null=True)  # Field name made lowercase.
    co_res1_029 = models.CharField(max_length=1000,db_column='CO_RES1_029', blank=True, null=True)  # Field name made lowercase.
    co_fun1_030 = models.CharField(max_length=1000,db_column='CO_FUN1_030', blank=True, null=True)  # Field name made lowercase.
    co_caf1_031 = models.CharField(max_length=1000,db_column='CO_CAF1_031', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_contactos_grilla'

#82
class IfCuerpo(models.Model):                       ### tabla con informacion importante 
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    cu_ortr_001 = models.DecimalField(db_column='CU_ORTR_001', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_anmp_002 = models.CharField(max_length=1000,db_column='CU_ANMP_002', blank=True, null=True)  # Field name made lowercase.
    cu_meth_003 = models.DecimalField(db_column='CU_METH_003', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_meep_004 = models.CharField(max_length=1000,db_column='CU_MEEP_004', blank=True, null=True)  # Field name made lowercase.
    cu_caar_005 = models.DecimalField(db_column='CU_CAAR_005', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_meta_006 = models.CharField(max_length=1000,db_column='CU_META_006', blank=True, null=True)  # Field name made lowercase.
    cu_metm_007 = models.DecimalField(db_column='CU_METM_007', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_meca_008 = models.CharField(max_length=1000,db_column='CU_MECA_008', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_cuerpo'

#83
class IfCuerpo2(models.Model):                       ### tabla con informacion importante
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    cu_metv_009 = models.DecimalField(db_column='CU_METV_009', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_mecv_010 = models.CharField(max_length=1000,db_column='CU_MECV_010', blank=True, null=True)  # Field name made lowercase.
    cu_mecp_011 = models.DecimalField(db_column='CU_MECP_011', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_meep_012 = models.CharField(max_length=1000,db_column='CU_MEEP_012', blank=True, null=True)  # Field name made lowercase.
    cu_anse_013 = models.CharField(max_length=1000,db_column='CU_ANSE_013', blank=True, null=True)  # Field name made lowercase.
    cu_meob_014 = models.CharField(max_length=1000,db_column='CU_MEOB_014', blank=True, null=True)  # Field name made lowercase.
    cu_mepe_015 = models.CharField(max_length=1000,db_column='CU_MEPE_015', blank=True, null=True)  # Field name made lowercase.
    cu_mela_016 = models.CharField(max_length=1000,db_column='CU_MELA_016', blank=True, null=True)  # Field name made lowercase.
    cu_ruta_017 = models.CharField(max_length=1000,db_column='CU_RUTA_017', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_cuerpo_2'

#84
class IfCuerpo3(models.Model):                           ### tabla con informacion importante
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    cu_hora_018 = models.CharField(max_length=1000,db_column='CU_HORA_018', blank=True, null=True)  # Field name made lowercase.
    cu_povu_019 = models.CharField(max_length=1000,db_column='CU_POVU_019', blank=True, null=True)  # Field name made lowercase.
    cu_obvu_020 = models.CharField(max_length=1000,db_column='CU_OBVU_020', blank=True, null=True)  # Field name made lowercase.
    cu_mbco_021 = models.DecimalField(db_column='CU_MBCO_021', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_mbas_022 = models.DecimalField(db_column='CU_MBAS_022', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_mbaa_023 = models.DecimalField(db_column='CU_MBAA_023', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_obco_024 = models.CharField(max_length=1000,db_column='CU_OBCO_024', blank=True, null=True)  # Field name made lowercase.
    cu_deau_025 = models.DecimalField(db_column='CU_DEAU_025', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_unidad_judicial = models.DecimalField(db_column='CU_UNIDAD_JUDICIAL', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'if_cuerpo_3'

#85
class IfCuerpo4(models.Model):                           ### tabla con informacion importante
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    cu_unju_026 = models.CharField(max_length=1000,db_column='CU_UNJU_026', blank=True, null=True)  # Field name made lowercase.
    cu_fedi_027 = models.DecimalField(db_column='CU_FEDI_027', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_feme_028 = models.DecimalField(db_column='CU_FEME_028', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_fean_029 = models.CharField(max_length=1000,db_column='CU_FEAN_029', blank=True, null=True)  # Field name made lowercase.
    cu_nupr_030 = models.CharField(max_length=1000,db_column='CU_NUPR_030', blank=True, null=True)  # Field name made lowercase.
    cu_deli_031 = models.CharField(max_length=1000,db_column='CU_DELI_031', blank=True, null=True)  # Field name made lowercase.
    cu_espr_032 = models.CharField(max_length=1000,db_column='CU_ESPR_032', blank=True, null=True)  # Field name made lowercase.
    cu_obde_033 = models.CharField(max_length=1000,db_column='CU_OBDE_033', blank=True, null=True)  # Field name made lowercase.
    cu_siin_034 = models.CharField(max_length=1000,db_column='CU_SIIN_034', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_cuerpo_4'

#86
class IfCuerpo5(models.Model):                           ### tabla con informacion importante
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    cu_rees_035 = models.CharField(max_length=1000,db_column='CU_REES_035', blank=True, null=True)  # Field name made lowercase.
    cu_anex_036 = models.CharField(max_length=1000,db_column='CU_ANEX_036', blank=True, null=True)  # Field name made lowercase.
    cu_narco_037 = models.DecimalField(db_column='CU_NARCO_037', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_anon_045 = models.DecimalField(db_column='CU_ANON_045', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_prof_053 = models.DecimalField(db_column='CU_PROF_053', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_subv_038 = models.DecimalField(db_column='CU_SUBV_038', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_cono_046 = models.DecimalField(db_column='CU_CONO_046', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_labo_054 = models.DecimalField(db_column='CU_LABO_054', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_grup_039 = models.DecimalField(db_column='CU_GRUP_039', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_escr_047 = models.DecimalField(db_column='CU_ESCR_047', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_pers_055 = models.DecimalField(db_column='CU_PERS_055', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_deli_040 = models.DecimalField(db_column='CU_DELI_040', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_tele_048 = models.DecimalField(db_column='CU_TELE_048', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_poli_056 = models.DecimalField(db_column='CU_POLI_056', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_deor_041 = models.DecimalField(db_column='CU_DEOR_041', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_medi_049 = models.DecimalField(db_column='CU_MEDI_049', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_econ_057 = models.DecimalField(db_column='CU_ECON_057', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_pers_042 = models.DecimalField(db_column='CU_PERS_042', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_info_050 = models.DecimalField(db_column='CU_INFO_050', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_idel_058 = models.DecimalField(db_column='CU_IDEL_058', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_fechaamenaza = models.DateField(db_column='CU_FECHAAMENAZA', blank=True, null=True)  # Field name made lowercase.
    cu_zonaamenaza = models.DecimalField(db_column='CU_ZONAAMENAZA', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'if_cuerpo_5'

#87
class IfCuerpo6(models.Model):                          ### tabla con informacion importante
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    cu_desc_043 = models.DecimalField(db_column='CU_DESC_043', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_obje_051 = models.DecimalField(db_column='CU_OBJE_051', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_otra_059 = models.DecimalField(db_column='CU_OTRA_059', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_otro_044 = models.DecimalField(db_column='CU_OTRO_044', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_verb_052 = models.DecimalField(db_column='CU_VERB_052', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cu_obca_060 = models.CharField(max_length=1000,db_column='CU_OBCA_060', blank=True, null=True)  # Field name made lowercase.
    cu_reac_061 = models.CharField(max_length=1000,db_column='CU_REAC_061', blank=True, null=True)  # Field name made lowercase.
    cu_anif_063 = models.CharField(max_length=1000,db_column='CU_ANIF_063', blank=True, null=True)  # Field name made lowercase.
    cu_nomb_062 = models.CharField(max_length=1000,db_column='CU_NOMB_062', blank=True, null=True)  # Field name made lowercase.
    cu_doid_063 = models.CharField(max_length=1000,db_column='CU_DOID_063', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_cuerpo_6'

#88
class IfCuerpo7(models.Model):                      ### tabla con informacion importante
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    cu_siinp2 = models.CharField(max_length=1000,db_column='CU_SIINP2', blank=True, null=True)  # Field name made lowercase.
    cu_siinp3 = models.CharField(max_length=1000,db_column='CU_SIINP3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_cuerpo_7'

#89
class IfDesplazamiento(models.Model):                ### tabla con informacion importante
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    de_ortr_001 = models.DecimalField(db_column='DE_ORTR_001', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_dfda_017 = models.DecimalField(db_column='DE_DFDA_017', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_mfda_018 = models.DecimalField(db_column='DE_MFDA_018', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_anda_019 = models.DecimalField(db_column='DE_ANDA_019', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_hoda_020 = models.DecimalField(db_column='DE_HODA_020', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_mida_021 = models.DecimalField(db_column='DE_MIDA_021', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_der1_026 = models.CharField(max_length=1000,db_column='DE_DER1_026', blank=True, null=True)  # Field name made lowercase.
    de_der2_027 = models.CharField(max_length=1000,db_column='DE_DER2_027', blank=True, null=True)  # Field name made lowercase.
    de_der3_028 = models.CharField(max_length=1000,db_column='DE_DER3_028', blank=True, null=True)  # Field name made lowercase.
    de_pmte_037 = models.DecimalField(db_column='DE_PMTE_037', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_tpue_038 = models.DecimalField(db_column='DE_TPUE_038', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_mtcp_039 = models.DecimalField(db_column='DE_MTCP_039', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_mtcu_040 = models.CharField(max_length=1000,db_column='DE_MTCU_040', blank=True, null=True)  # Field name made lowercase.
    de_mtmp_041 = models.DecimalField(db_column='DE_MTMP_041', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_mtot_042 = models.DecimalField(db_column='DE_MTOT_042', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_mtcu_043 = models.CharField(max_length=1000,db_column='DE_MTCU_043', blank=True, null=True)  # Field name made lowercase.
    de_dare_044 = models.DecimalField(db_column='DE_DARE_044', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_trut_047 = models.DecimalField(db_column='DE_TRUT_047', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_tmco_050 = models.CharField(max_length=1000,db_column='DE_TMCO_050', blank=True, null=True)  # Field name made lowercase.
    de_noan_055 = models.CharField(max_length=1000,db_column='DE_NOAN_055', blank=True, null=True)  # Field name made lowercase.
    de_doan_056 = models.CharField(max_length=1000,db_column='DE_DOAN_056', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_desplazamiento'

#90
class IfDesplazamientoGrilla(models.Model):          ### tabla con informacion para las celdas
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    de_inru_055 = models.DecimalField(db_column='DE_INRU_055', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_rut1_023 = models.DecimalField(db_column='DE_RUT1_023', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_rut2_024 = models.DecimalField(db_column='DE_RUT2_024', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    de_rut3_025 = models.DecimalField(db_column='DE_RUT3_025', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'if_desplazamiento_grilla'

#91
class IfDocumental(models.Model):                    ### tabla con informacion para las celdas
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    do_ortr_001 = models.DecimalField(db_column='DO_ORTR_001', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    do_fure_023 = models.CharField(max_length=1000,db_column='DO_FURE_023', blank=True, null=True)  # Field name made lowercase.
    do_fuca_024 = models.CharField(max_length=1000,db_column='DO_FUCA_024', blank=True, null=True)  # Field name made lowercase.
    do_fudo_025 = models.CharField(max_length=1000,db_column='DO_FUDO_025', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_documental'

#92
class IfDocumentalGrilla(models.Model):              ### tabla con informacion importante
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    do_cofu_026 = models.DecimalField(db_column='DO_COFU_026', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    do_fudo_017 = models.CharField(max_length=1000,db_column='DO_FUDO_017', blank=True, null=True)  # Field name made lowercase.
    do_nodo_018 = models.CharField(max_length=1000,db_column='DO_NODO_018', blank=True, null=True)  # Field name made lowercase.
    do_dico_019 = models.DecimalField(db_column='DO_DICO_019', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    do_medo_020 = models.DecimalField(db_column='DO_MEDO_020', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    do_ando_021 = models.DecimalField(db_column='DO_ANDO_021', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    do_redo_022 = models.CharField(max_length=1000,db_column='DO_REDO_022', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_documental_grilla'

#93
class IfDrecEvaluados(models.Model):                ### tabla con informacion para las celdas
    if_drec_id = models.AutoField(primary_key=True)
    if_drec_nromemo = models.CharField(max_length=1000,blank=True, null=True)
    if_drec_tipodoc = models.DecimalField(max_digits=30, decimal_places=6, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_drec_numdocumeto = models.CharField(max_length=1000,blank=True, null=True)
    if_drec_pnombre = models.CharField(max_length=1000,blank=True, null=True)
    if_drec_snombre = models.CharField(max_length=1000,blank=True, null=True)
    if_drec_papellido = models.CharField(max_length=1000,blank=True, null=True)
    if_drec_sapellido = models.CharField(max_length=1000,blank=True, null=True)
    if_drec_tiporeval = models.DecimalField(max_digits=30, decimal_places=6, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_drec_estado = models.DecimalField(max_digits=30, decimal_places=6, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_drec_analistarep = models.DecimalField(max_digits=30, decimal_places=6, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_drec_ot = models.DecimalField(db_column='if_drec_OT', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_drec_fecharegistro = models.DateField(blank=True, null=True)
    if_drec_fechaenvio = models.DateField(blank=True, null=True)
    if_drec_fechadevuelto = models.DateField(blank=True, null=True)
    if_drec_fechaaceptado = models.DateField(blank=True, null=True)
    if_mrec_secue = models.IntegerField(blank=True, null=True)
    if_drec_tipodev = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_drec_descdev = models.CharField(max_length=1000,blank=True, null=True)
    if_drec_depto = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_drec_municipio = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_drec_grupopob = models.CharField(max_length=1000,blank=True, null=True)
    if_drec_categoria = models.CharField(max_length=1000,blank=True, null=True)
    if_drec_subcategoria = models.CharField(max_length=1000,blank=True, null=True)
    if_drec_analistaasigna = models.CharField(max_length=1000,blank=True, null=True)
    if_drec_nrofolio = models.IntegerField(blank=True, null=True)
    if_drec_anexo = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_drec_tipo_evaluacion = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_drec_nromemo_devol = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'if_drec_evaluados'

#94
class IfEntornos(models.Model):                     ### tabla con informacion importante
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    et_didi_001 = models.DecimalField(db_column='ET_DIDI_001', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_dime_002 = models.DecimalField(db_column='ET_DIME_002', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_dian_003 = models.CharField(max_length=1000,db_column='ET_DIAN_003', blank=True, null=True)  # Field name made lowercase.
    et_didi_004 = models.DecimalField(db_column='ET_DIDI_004', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_dime_005 = models.DecimalField(db_column='ET_DIME_005', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_dian_006 = models.CharField(max_length=1000,db_column='ET_DIAN_006', blank=True, null=True)  # Field name made lowercase.
    et_dire_007 = models.CharField(max_length=1000,db_column='ET_DIRE_007', blank=True, null=True)  # Field name made lowercase.
    et_ditr_008 = models.CharField(max_length=1000,db_column='ET_DITR_008', blank=True, null=True)  # Field name made lowercase.
    et_dere_009 = models.DecimalField(db_column='ET_DERE_009', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_mure_010 = models.DecimalField(db_column='ET_MURE_010', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_detr_011 = models.DecimalField(db_column='ET_DETR_011', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_mutr_012 = models.DecimalField(db_column='ET_MUTR_012', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_dicu_013 = models.CharField(max_length=1000,db_column='ET_DICU_013', blank=True, null=True)  # Field name made lowercase.
    et_sice_014 = models.DecimalField(db_column='ET_SICE_014', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_zour_015 = models.DecimalField(db_column='ET_ZOUR_015', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_zuob_016 = models.CharField(max_length=1000,db_column='ET_ZUOB_016', blank=True, null=True)  # Field name made lowercase.
    et_zutr_017 = models.DecimalField(db_column='ET_ZUTR_017', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_zuto_018 = models.CharField(max_length=1000,db_column='ET_ZUTO_018', blank=True, null=True)  # Field name made lowercase.
    et_diso_031 = models.DecimalField(db_column='ET_DISO_031', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_meso_032 = models.DecimalField(db_column='ET_MESO_032', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_anso_033 = models.CharField(max_length=1000,db_column='ET_ANSO_033', blank=True, null=True)  # Field name made lowercase.
    et_reve_034 = models.CharField(max_length=1000,db_column='ET_REVE_034', blank=True, null=True)  # Field name made lowercase.
    et_rect_035 = models.CharField(max_length=1000,db_column='ET_RECT_035', blank=True, null=True)  # Field name made lowercase.
    et_rees_036 = models.CharField(max_length=1000,db_column='ET_REES_036', blank=True, null=True)  # Field name made lowercase.
    et_stco_037 = models.CharField(max_length=1000,db_column='ET_STCO_037', blank=True, null=True)  # Field name made lowercase.
    et_perf_038 = models.CharField(max_length=1000,db_column='ET_PERF_038', blank=True, null=True)  # Field name made lowercase.
    et_noan_005 = models.CharField(max_length=1000,db_column='ET_NOAN_005', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_entornos'

#95
class IfEntornosGrilal2(models.Model):              ### tabla con informacion para las celdas
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    et_nupr_025 = models.DecimalField(db_column='ET_NUPR_025', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_snre_027 = models.DecimalField(db_column='ET_SNRE_027', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_obr2_028 = models.CharField(max_length=1000,db_column='ET_OBR2_028', blank=True, null=True)  # Field name made lowercase.
    et_snt2_029 = models.DecimalField(db_column='ET_SNT2_029', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_ont2_030 = models.CharField(max_length=1000,db_column='ET_ONT2_030', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_entornos_grilal2'

#96
class IfEntornosGrilla(models.Model):               ### tabla con informacion para las celdas
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    et_nupr_019 = models.DecimalField(db_column='ET_NUPR_019', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_snre_021 = models.DecimalField(db_column='ET_SNRE_021', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_obre_022 = models.CharField(max_length=1000,db_column='ET_OBRE_022', blank=True, null=True)  # Field name made lowercase.
    et_sntr_023 = models.DecimalField(db_column='ET_SNTR_023', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    et_obtr_024 = models.CharField(max_length=1000,db_column='ET_OBTR_024', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_entornos_grilla'

#97
class IfEntrevisataGrilla1(models.Model):           ### tabla con informacion para las celdas  
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    en_cohi_164 = models.DecimalField(db_column='EN_COHI_164', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_hiev_108 = models.CharField(max_length=1000,db_column='EN_HIEV_108', blank=True, null=True)  # Field name made lowercase.
    en_edhi_109 = models.DecimalField(db_column='EN_EDHI_109', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_achi_110 = models.CharField(max_length=1000,db_column='EN_ACHI_110', blank=True, null=True)  # Field name made lowercase.
    en_rehi_111 = models.CharField(max_length=1000,db_column='EN_REHI_111', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_entrevisata_grilla1'

#98
class IfEntrevisataGrilla2(models.Model):           ### tabla con informacion para las celdas
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    en_cola_165 = models.CharField(max_length=1000,db_column='EN_COLA_165', blank=True, null=True)  # Field name made lowercase.
    en_emhl_123 = models.CharField(max_length=1000,db_column='EN_EMHL_123', blank=True, null=True)  # Field name made lowercase.
    en_dehl_124 = models.CharField(max_length=1000,db_column='EN_DEHL_124', blank=True, null=True)  # Field name made lowercase.
    en_muhl_125 = models.CharField(max_length=1000,db_column='EN_MUHL_125', blank=True, null=True)  # Field name made lowercase.
    en_cahl_126 = models.CharField(max_length=1000,db_column='EN_CAHL_126', blank=True, null=True)  # Field name made lowercase.
    en_pehl_127 = models.CharField(max_length=1000,db_column='EN_PEHL_127', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_entrevisata_grilla2'

#99
class IfEntrevista(models.Model):                   ### tabla con informacion importante
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    en_ortr_001 = models.DecimalField(db_column='EN_ORTR_001', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_deen_011 = models.DecimalField(db_column='EN_DEEN_011', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_muen_012 = models.DecimalField(db_column='EN_MUEN_012', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_dien_013 = models.CharField(max_length=1000,db_column='EN_DIEN_013', blank=True, null=True)  # Field name made lowercase.
    en_zoen_014 = models.DecimalField(db_column='EN_ZOEN_014', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_dien_015 = models.DecimalField(db_column='EN_DIEN_015', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_meen_016 = models.DecimalField(db_column='EN_MEEN_016', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_anen_017 = models.DecimalField(db_column='EN_ANEN_017', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_hoen_018 = models.DecimalField(db_column='EN_HOEN_018', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_mien_019 = models.DecimalField(db_column='EN_MIEN_019', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_pnen_020 = models.CharField(max_length=1000,db_column='EN_PNEN_020', blank=True, null=True)  # Field name made lowercase.
    en_smen_021 = models.CharField(max_length=1000,db_column='EN_SMEN_021', blank=True, null=True)  # Field name made lowercase.
    en_paen_022 = models.CharField(max_length=1000,db_column='EN_PAEN_022', blank=True, null=True)  # Field name made lowercase.
    en_saen_023 = models.CharField(max_length=1000,db_column='EN_SAEN_023', blank=True, null=True)  # Field name made lowercase.
    en_tien_024 = models.DecimalField(db_column='EN_TIEN_024', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_nien_025 = models.CharField(max_length=1000,db_column='EN_NIEN_025', blank=True, null=True)  # Field name made lowercase.
    en_dnac_026 = models.DecimalField(db_column='EN_DNAC_026', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_mnac_027 = models.DecimalField(db_column='EN_MNAC_027', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_anac_028 = models.DecimalField(db_column='EN_ANAC_028', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_edad_291 = models.DecimalField(db_column='EN_EDAD_291', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_dnac_029 = models.DecimalField(db_column='EN_DNAC_029', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_mnac_030 = models.DecimalField(db_column='EN_MNAC_030', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_sexo_031 = models.DecimalField(db_column='EN_SEXO_031', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_esci_032 = models.DecimalField(db_column='EN_ESCI_032', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_niac_033 = models.DecimalField(db_column='EN_NIAC_033', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_tall_331 = models.DecimalField(db_column='EN_TALL_331', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_esta_332 = models.DecimalField(db_column='EN_ESTA_332', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_tisa_034 = models.DecimalField(db_column='EN_TISA_034', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_rhen_035 = models.DecimalField(db_column='EN_RHEN_035', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_deal_036 = models.DecimalField(db_column='EN_DEAL_036', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_mual_037 = models.DecimalField(db_column='EN_MUAL_037', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_prfe_038 = models.CharField(max_length=1000,db_column='EN_PRFE_038', blank=True, null=True)  # Field name made lowercase.
    en_ofic_039 = models.CharField(max_length=1000,db_column='EN_OFIC_039', blank=True, null=True)  # Field name made lowercase.
    en_dial_040 = models.CharField(max_length=1000,db_column='EN_DIAL_040', blank=True, null=True)  # Field name made lowercase.
    en_teal_041 = models.CharField(max_length=1000,db_column='EN_TEAL_041', blank=True, null=True)  # Field name made lowercase.
    en_dere_042 = models.DecimalField(db_column='EN_DERE_042', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_mure_043 = models.DecimalField(db_column='EN_MURE_043', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_dire_044 = models.CharField(max_length=1000,db_column='EN_DIRE_044', blank=True, null=True)  # Field name made lowercase.
    en_tfre_045 = models.CharField(max_length=1000,db_column='EN_TFRE_045', blank=True, null=True)  # Field name made lowercase.
    en_tcre_046 = models.CharField(max_length=1000,db_column='EN_TCRE_046', blank=True, null=True)  # Field name made lowercase.
    en_cere_047 = models.CharField(max_length=1000,db_column='EN_CERE_047', blank=True, null=True)  # Field name made lowercase.
    en_napc_048 = models.CharField(max_length=1000,db_column='EN_NAPC_048', blank=True, null=True)  # Field name made lowercase.
    en_tfpc_049 = models.CharField(max_length=1000,db_column='EN_TFPC_049', blank=True, null=True)  # Field name made lowercase.
    en_tcpc_050 = models.CharField(max_length=1000,db_column='EN_TCPC_050', blank=True, null=True)  # Field name made lowercase.
    en_depc_051 = models.DecimalField(db_column='EN_DEPC_051', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_mupc_052 = models.DecimalField(db_column='EN_MUPC_052', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_dipc_053 = models.CharField(max_length=1000,db_column='EN_DIPC_053', blank=True, null=True)  # Field name made lowercase.
    en_papc_054 = models.CharField(max_length=1000,db_column='EN_PAPC_054', blank=True, null=True)  # Field name made lowercase.
    en_nppc_055 = models.CharField(max_length=1000,db_column='EN_NPPC_055', blank=True, null=True)  # Field name made lowercase.
    en_enob_056 = models.CharField(max_length=1000,db_column='EN_ENOB_056', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_entrevista'

#100
class IfEntrevista2(models.Model):                   ### tabla con informacion importante
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=30, decimal_places=6)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=30, decimal_places=6)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=30, decimal_places=6)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=30, decimal_places=6)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=30, decimal_places=6)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=30, decimal_places=6)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    en_tigp_057 = models.DecimalField(db_column='EN_TIGP_057', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpdp_058 = models.DecimalField(db_column='EN_GPDP_058', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpov_070 = models.DecimalField(db_column='EN_GPOV_070', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpdp_059 = models.DecimalField(db_column='EN_GPDP_059', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpsp_071 = models.DecimalField(db_column='EN_GPSP_071', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpco_060 = models.DecimalField(db_column='EN_GPCO_060', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpes_072 = models.DecimalField(db_column='EN_GPES_072', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpos_061 = models.DecimalField(db_column='EN_GPOS_061', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpap_073 = models.DecimalField(db_column='EN_GPAP_073', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpsi_062 = models.DecimalField(db_column='EN_GPSI_062', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpup_074 = models.DecimalField(db_column='EN_GPUP_074', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpog_063 = models.DecimalField(db_column='EN_GPOG_063', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpad_075 = models.DecimalField(db_column='EN_GPAD_075', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpge_064 = models.DecimalField(db_column='EN_GPGE_064', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpdo_076 = models.DecimalField(db_column='EN_GPDO_076', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpdh_066 = models.DecimalField(db_column='EN_GPDH_066', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpos_077 = models.DecimalField(db_column='EN_GPOS_077', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gppd_067 = models.DecimalField(db_column='EN_GPPD_067', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpda_078 = models.DecimalField(db_column='EN_GPDA_078', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gprt_068 = models.DecimalField(db_column='EN_GPRT_068', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpfd_079 = models.DecimalField(db_column='EN_GPFD_079', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpcp_069 = models.DecimalField(db_column='EN_GPCP_069', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpcc_080 = models.DecimalField(db_column='EN_GPCC_080', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_gpmm_065 = models.DecimalField(db_column='EN_GPMM_065', max_digits=30, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_escc_081 = models.CharField(max_length=1000,db_column='EN_ESCC_081', blank=True, null=True)  # Field name made lowercase.
    en_obgp_082 = models.CharField(max_length=1000,db_column='EN_OBGP_082', blank=True, null=True)  # Field name made lowercase.
    en_tigp_057_historico = models.DecimalField(db_column='EN_TIGP_057_HISTORICO', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'if_entrevista_2'

#101
class IfEntrevista3(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    en_maho_083 = models.DecimalField(db_column='EN_MAHO_083', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_pete_089 = models.DecimalField(db_column='EN_PETE_089', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_viud_084 = models.DecimalField(db_column='EN_VIUD_084', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_pedi_090 = models.DecimalField(db_column='EN_PEDI_090', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_muge_085 = models.DecimalField(db_column='EN_MUGE_085', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_plgt_091 = models.DecimalField(db_column='EN_PLGT_091', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_mula_086 = models.DecimalField(db_column='EN_MULA_086', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_afro_092 = models.DecimalField(db_column='EN_AFRO_092', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_mame_087 = models.DecimalField(db_column='EN_MAME_087', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_indi_093 = models.DecimalField(db_column='EN_INDI_093', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_home_088 = models.DecimalField(db_column='EN_HOME_088', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_nonr_094 = models.DecimalField(db_column='EN_NONR_094', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_obse_095 = models.CharField(max_length=1000,db_column='EN_OBSE_095', blank=True, null=True)  # Field name made lowercase.
    en_noco_096 = models.CharField(max_length=1000,db_column='EN_NOCO_096', blank=True, null=True)  # Field name made lowercase.
    en_apco_097 = models.CharField(max_length=1000,db_column='EN_APCO_097', blank=True, null=True)  # Field name made lowercase.
    en_tico_098 = models.DecimalField(db_column='EN_TICO_098', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_nico_099 = models.CharField(max_length=1000,db_column='EN_NICO_099', blank=True, null=True)  # Field name made lowercase.
    en_tfco_100 = models.CharField(max_length=1000,db_column='EN_TFCO_100', blank=True, null=True)  # Field name made lowercase.
    en_tcco_101 = models.CharField(max_length=1000,db_column='EN_TCCO_101', blank=True, null=True)  # Field name made lowercase.
    en_deco_102 = models.DecimalField(db_column='EN_DECO_102', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_muco_103 = models.DecimalField(db_column='EN_MUCO_103', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_dico_104 = models.CharField(max_length=1000,db_column='EN_DICO_104', blank=True, null=True)  # Field name made lowercase.
    en_occo_105 = models.CharField(max_length=1000,db_column='EN_OCCO_105', blank=True, null=True)  # Field name made lowercase.
    en_emco_106 = models.CharField(max_length=1000,db_column='EN_EMCO_106', blank=True, null=True)  # Field name made lowercase.
    en_cafa_107 = models.CharField(max_length=1000,db_column='EN_CAFA_107', blank=True, null=True)  # Field name made lowercase.
    en_pano_112 = models.CharField(max_length=1000,db_column='EN_PANO_112', blank=True, null=True)  # Field name made lowercase.
    en_paoc_113 = models.CharField(max_length=1000,db_column='EN_PAOC_113', blank=True, null=True)  # Field name made lowercase.
    en_cafp_114 = models.CharField(max_length=1000,db_column='EN_CAFP_114', blank=True, null=True)  # Field name made lowercase.
    en_noma_115 = models.CharField(max_length=1000,db_column='EN_NOMA_115', blank=True, null=True)  # Field name made lowercase.
    en_ocma_116 = models.CharField(max_length=1000,db_column='EN_OCMA_116', blank=True, null=True)  # Field name made lowercase.
    en_cafm_117 = models.CharField(max_length=1000,db_column='EN_CAFM_117', blank=True, null=True)  # Field name made lowercase.
    en_opdd_118 = models.CharField(max_length=1000,db_column='EN_OPDD_118', blank=True, null=True)  # Field name made lowercase.
    en_inam_119 = models.CharField(max_length=1000,db_column='EN_INAM_119', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_entrevista_3'

#102
class IfEntrevista4(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    en_sidi_120 = models.DecimalField(db_column='EN_SIDI_120', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_esdi_121 = models.CharField(max_length=1000,db_column='EN_ESDI_121', blank=True, null=True)  # Field name made lowercase.
    en_obev_122 = models.CharField(max_length=1000,db_column='EN_OBEV_122', blank=True, null=True)  # Field name made lowercase.
    en_obhl_128 = models.CharField(max_length=1000,db_column='EN_OBHL_128', blank=True, null=True)  # Field name made lowercase.
    en_apmp_129 = models.DecimalField(db_column='EN_APMP_129', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_caaf_130 = models.CharField(max_length=1000,db_column='EN_CAAF_130', blank=True, null=True)  # Field name made lowercase.
    en_meem_131 = models.DecimalField(db_column='EN_MEEM_131', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_caam_132 = models.CharField(max_length=1000,db_column='EN_CAAM_132', blank=True, null=True)  # Field name made lowercase.
    en_anmp_133 = models.CharField(max_length=1000,db_column='EN_ANMP_133', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_entrevista_4'

#103
class IfEntrevista5(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    en_mees_134 = models.CharField(max_length=1000,db_column='EN_MEES_134', blank=True, null=True)  # Field name made lowercase.
    en_moap_135 = models.CharField(max_length=1000,db_column='EN_MOAP_135', blank=True, null=True)  # Field name made lowercase.
    en_moal_136 = models.CharField(max_length=1000,db_column='EN_MOAL_136', blank=True, null=True)  # Field name made lowercase.
    en_ruta_137 = models.CharField(max_length=1000,db_column='EN_RUTA_137', blank=True, null=True)  # Field name made lowercase.
    en_hora_138 = models.CharField(max_length=1000,db_column='EN_HORA_138', blank=True, null=True)  # Field name made lowercase.
    en_povu_139 = models.CharField(max_length=1000,db_column='EN_POVU_139', blank=True, null=True)  # Field name made lowercase.
    en_obvu_140 = models.CharField(max_length=1000,db_column='EN_OBVU_140', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_entrevista_5'

#104
class IfEntrevista6(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    en_enre_141 = models.CharField(max_length=1000,db_column='EN_ENRE_141', blank=True, null=True)  # Field name made lowercase.
    en_enla_142 = models.CharField(max_length=1000,db_column='EN_ENLA_142', blank=True, null=True)  # Field name made lowercase.
    en_enso_143 = models.CharField(max_length=1000,db_column='EN_ENSO_143', blank=True, null=True)  # Field name made lowercase.
    en_cono_144 = models.DecimalField(db_column='EN_CONO_144', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_apli_145 = models.DecimalField(db_column='EN_APLI_145', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_alve_146 = models.DecimalField(db_column='EN_ALVE_146', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_obco_147 = models.CharField(max_length=1000,db_column='EN_OBCO_147', blank=True, null=True)  # Field name made lowercase.
    en_deac_148 = models.DecimalField(db_column='EN_DEAC_148', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_unju_149 = models.CharField(max_length=1000,db_column='EN_UNJU_149', blank=True, null=True)  # Field name made lowercase.
    en_dide_150 = models.DecimalField(db_column='EN_DIDE_150', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_mede_151 = models.DecimalField(db_column='EN_MEDE_151', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_ande_152 = models.CharField(max_length=1000,db_column='EN_ANDE_152', blank=True, null=True)  # Field name made lowercase.
    en_nupr_153 = models.CharField(max_length=1000,db_column='EN_NUPR_153', blank=True, null=True)  # Field name made lowercase.
    en_deli_154 = models.CharField(max_length=1000,db_column='EN_DELI_154', blank=True, null=True)  # Field name made lowercase.
    en_espr_155 = models.CharField(max_length=1000,db_column='EN_ESPR_155', blank=True, null=True)  # Field name made lowercase.
    en_obde_156 = models.CharField(max_length=1000,db_column='EN_OBDE_156', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_entrevista_6'

#105
class IfEntrevista7(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    en_siin_157 = models.CharField(max_length=1000,db_column='EN_SIIN_157', blank=True, null=True)  # Field name made lowercase.
    en_rees_158 = models.CharField(max_length=1000,db_column='EN_REES_158', blank=True, null=True)  # Field name made lowercase.
    en_anex_159 = models.CharField(max_length=1000,db_column='EN_ANEX_159', blank=True, null=True)  # Field name made lowercase.
    en_noev_160 = models.CharField(max_length=1000,db_column='EN_NOEV_160', blank=True, null=True)  # Field name made lowercase.
    en_nofu_162 = models.CharField(max_length=1000,db_column='EN_NOFU_162', blank=True, null=True)  # Field name made lowercase.
    en_doev_161 = models.CharField(max_length=1000,db_column='EN_DOEV_161', blank=True, null=True)  # Field name made lowercase.
    en_difu_163 = models.CharField(max_length=1000,db_column='EN_DIFU_163', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_entrevista_7'

#106
class IfEntrevista8(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    en_siinp2 = models.CharField(max_length=1000,db_column='EN_SIINP2', blank=True, null=True)  # Field name made lowercase.
    en_siinp3 = models.CharField(max_length=1000,db_column='EN_SIINP3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_entrevista_8'

#107
class IfEscoltas(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    ee_ortr_001 = models.DecimalField(db_column='EE_ORTR_001', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_dfda_017 = models.DecimalField(db_column='EE_DFDA_017', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_mfda_018 = models.DecimalField(db_column='EE_MFDA_018', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_afda_019 = models.DecimalField(db_column='EE_AFDA_019', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_hfda_020 = models.DecimalField(db_column='EE_HFDA_020', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_mifd_021 = models.DecimalField(db_column='EE_MIFD_021', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_lerp_022 = models.CharField(max_length=1000,db_column='EE_LERP_022', blank=True, null=True)  # Field name made lowercase.
    ee_ntdo_028 = models.CharField(max_length=1000,db_column='EE_NTDO_028', blank=True, null=True)  # Field name made lowercase.
    ee_derp_023 = models.DecimalField(db_column='EE_DERP_023', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_ntde_029 = models.CharField(max_length=1000,db_column='EE_NTDE_029', blank=True, null=True)  # Field name made lowercase.
    ee_merp_024 = models.DecimalField(db_column='EE_MERP_024', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_nipe_026 = models.CharField(max_length=1000,db_column='EE_NIPE_026', blank=True, null=True)  # Field name made lowercase.
    ee_ecad_027 = models.DecimalField(db_column='EE_ECAD_027', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_pnpo_025 = models.CharField(max_length=1000,db_column='EE_PNPO_025', blank=True, null=True)  # Field name made lowercase.
    ee_snpo_025 = models.CharField(max_length=1000,db_column='EE_SNPO_025', blank=True, null=True)  # Field name made lowercase.
    ee_papo_025 = models.CharField(max_length=1000,db_column='EE_PAPO_025', blank=True, null=True)  # Field name made lowercase.
    ee_sapo_025 = models.CharField(max_length=1000,db_column='EE_SAPO_025', blank=True, null=True)  # Field name made lowercase.
    ee_pnpo_030 = models.CharField(max_length=1000,db_column='EE_PNPO_030', blank=True, null=True)  # Field name made lowercase.
    ee_snpo_030 = models.CharField(max_length=1000,db_column='EE_SNPO_030', blank=True, null=True)  # Field name made lowercase.
    ee_papr_030 = models.CharField(max_length=1000,db_column='EE_PAPR_030', blank=True, null=True)  # Field name made lowercase.
    ee_sapr_030 = models.CharField(max_length=1000,db_column='EE_SAPR_030', blank=True, null=True)  # Field name made lowercase.
    ee_ties_031 = models.DecimalField(db_column='EE_TIES_031', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_nies_032 = models.DecimalField(db_column='EE_NIES_032', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_noin_033 = models.CharField(max_length=1000,db_column='EE_NOIN_033', blank=True, null=True)  # Field name made lowercase.
    ee_noin_044 = models.CharField(max_length=1000,db_column='EE_NOIN_044', blank=True, null=True)  # Field name made lowercase.
    ee_noin_055 = models.CharField(max_length=1000,db_column='EE_NOIN_055', blank=True, null=True)  # Field name made lowercase.
    ee_cein_034 = models.CharField(max_length=1000,db_column='EE_CEIN_034', blank=True, null=True)  # Field name made lowercase.
    ee_cein_045 = models.CharField(max_length=1000,db_column='EE_CEIN_045', blank=True, null=True)  # Field name made lowercase.
    ee_cein_056 = models.CharField(max_length=1000,db_column='EE_CEIN_056', blank=True, null=True)  # Field name made lowercase.
    ee_plin_035 = models.CharField(max_length=1000,db_column='EE_PLIN_035', blank=True, null=True)  # Field name made lowercase.
    ee_plin_046 = models.CharField(max_length=1000,db_column='EE_PLIN_046', blank=True, null=True)  # Field name made lowercase.
    ee_plin_057 = models.CharField(max_length=1000,db_column='EE_PLIN_057', blank=True, null=True)  # Field name made lowercase.
    ee_enin_036 = models.CharField(max_length=1000,db_column='EE_ENIN_036', blank=True, null=True)  # Field name made lowercase.
    ee_enin_047 = models.CharField(max_length=1000,db_column='EE_ENIN_047', blank=True, null=True)  # Field name made lowercase.
    ee_enin_058 = models.CharField(max_length=1000,db_column='EE_ENIN_058', blank=True, null=True)  # Field name made lowercase.
    ee_fcin_058 = models.CharField(max_length=1000,db_column='EE_FCIN_058', blank=True, null=True)  # Field name made lowercase.
    ee_fcin_059 = models.CharField(max_length=1000,db_column='EE_FCIN_059', blank=True, null=True)  # Field name made lowercase.
    ee_fcin_060 = models.CharField(max_length=1000,db_column='EE_FCIN_060', blank=True, null=True)  # Field name made lowercase.
    ee_cumc_037 = models.DecimalField(db_column='EE_CUMC_037', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_cumc_048 = models.DecimalField(db_column='EE_CUMC_048', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_cumc_059 = models.DecimalField(db_column='EE_CUMC_059', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_nomc_038 = models.CharField(max_length=1000,db_column='EE_NOMC_038', blank=True, null=True)  # Field name made lowercase.
    ee_nomc_049 = models.CharField(max_length=1000,db_column='EE_NOMC_049', blank=True, null=True)  # Field name made lowercase.
    ee_nomc_060 = models.CharField(max_length=1000,db_column='EE_NOMC_060', blank=True, null=True)  # Field name made lowercase.
    ee_ccar_039 = models.DecimalField(db_column='EE_CCAR_039', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_ccar_050 = models.DecimalField(db_column='EE_CCAR_050', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_ccar_061 = models.DecimalField(db_column='EE_CCAR_061', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_caar_040 = models.CharField(max_length=1000,db_column='EE_CAAR_040', blank=True, null=True)  # Field name made lowercase.
    ee_caar_051 = models.CharField(max_length=1000,db_column='EE_CAAR_051', blank=True, null=True)  # Field name made lowercase.
    ee_caar_062 = models.CharField(max_length=1000,db_column='EE_CAAR_062', blank=True, null=True)  # Field name made lowercase.
    ee_nsar_041 = models.CharField(max_length=1000,db_column='EE_NSAR_041', blank=True, null=True)  # Field name made lowercase.
    ee_nsar_052 = models.CharField(max_length=1000,db_column='EE_NSAR_052', blank=True, null=True)  # Field name made lowercase.
    ee_nsar_063 = models.CharField(max_length=1000,db_column='EE_NSAR_063', blank=True, null=True)  # Field name made lowercase.
    ee_ncar_042 = models.CharField(max_length=1000,db_column='EE_NCAR_042', blank=True, null=True)  # Field name made lowercase.
    ee_ncar_053 = models.CharField(max_length=1000,db_column='EE_NCAR_053', blank=True, null=True)  # Field name made lowercase.
    ee_ncar_064 = models.CharField(max_length=1000,db_column='EE_NCAR_064', blank=True, null=True)  # Field name made lowercase.
    ee_ccch_043 = models.DecimalField(db_column='EE_CCCH_043', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_ccch_054 = models.DecimalField(db_column='EE_CCCH_054', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_ccch_065 = models.DecimalField(db_column='EE_CCCH_065', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_noin_066 = models.CharField(max_length=1000,db_column='EE_NOIN_066', blank=True, null=True)  # Field name made lowercase.
    ee_noin_077 = models.CharField(max_length=1000,db_column='EE_NOIN_077', blank=True, null=True)  # Field name made lowercase.
    ee_noin_088 = models.CharField(max_length=1000,db_column='EE_NOIN_088', blank=True, null=True)  # Field name made lowercase.
    ee_cein_067 = models.CharField(max_length=1000,db_column='EE_CEIN_067', blank=True, null=True)  # Field name made lowercase.
    ee_cein_078 = models.CharField(max_length=1000,db_column='EE_CEIN_078', blank=True, null=True)  # Field name made lowercase.
    ee_cein_089 = models.CharField(max_length=1000,db_column='EE_CEIN_089', blank=True, null=True)  # Field name made lowercase.
    ee_plin_068 = models.CharField(max_length=1000,db_column='EE_PLIN_068', blank=True, null=True)  # Field name made lowercase.
    ee_plin_079 = models.CharField(max_length=1000,db_column='EE_PLIN_079', blank=True, null=True)  # Field name made lowercase.
    ee_plin_090 = models.CharField(max_length=1000,db_column='EE_PLIN_090', blank=True, null=True)  # Field name made lowercase.
    ee_enin_069 = models.CharField(max_length=1000,db_column='EE_ENIN_069', blank=True, null=True)  # Field name made lowercase.
    ee_enin_080 = models.CharField(max_length=1000,db_column='EE_ENIN_080', blank=True, null=True)  # Field name made lowercase.
    ee_enin_091 = models.CharField(max_length=1000,db_column='EE_ENIN_091', blank=True, null=True)  # Field name made lowercase.
    ee_fnin_091 = models.CharField(max_length=1000,db_column='EE_FNIN_091', blank=True, null=True)  # Field name made lowercase.
    ee_fnin_092 = models.CharField(max_length=1000,db_column='EE_FNIN_092', blank=True, null=True)  # Field name made lowercase.
    ee_fnin_093 = models.CharField(max_length=1000,db_column='EE_FNIN_093', blank=True, null=True)  # Field name made lowercase.
    ee_cumc_070 = models.DecimalField(db_column='EE_CUMC_070', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_cumc_081 = models.DecimalField(db_column='EE_CUMC_081', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_cumc_092 = models.DecimalField(db_column='EE_CUMC_092', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_nomc_071 = models.CharField(max_length=1000,db_column='EE_NOMC_071', blank=True, null=True)  # Field name made lowercase.
    ee_nomc_082 = models.CharField(max_length=1000,db_column='EE_NOMC_082', blank=True, null=True)  # Field name made lowercase.
    ee_nomc_093 = models.CharField(max_length=1000,db_column='EE_NOMC_093', blank=True, null=True)  # Field name made lowercase.
    ee_ccar_072 = models.DecimalField(db_column='EE_CCAR_072', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_ccar_083 = models.DecimalField(db_column='EE_CCAR_083', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_ccar_094 = models.DecimalField(db_column='EE_CCAR_094', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_caar_073 = models.CharField(max_length=1000,db_column='EE_CAAR_073', blank=True, null=True)  # Field name made lowercase.
    ee_caar_084 = models.CharField(max_length=1000,db_column='EE_CAAR_084', blank=True, null=True)  # Field name made lowercase.
    ee_caar_095 = models.CharField(max_length=1000,db_column='EE_CAAR_095', blank=True, null=True)  # Field name made lowercase.
    ee_nsar_074 = models.CharField(max_length=1000,db_column='EE_NSAR_074', blank=True, null=True)  # Field name made lowercase.
    ee_nsar_085 = models.CharField(max_length=1000,db_column='EE_NSAR_085', blank=True, null=True)  # Field name made lowercase.
    ee_nsar_096 = models.CharField(max_length=1000,db_column='EE_NSAR_096', blank=True, null=True)  # Field name made lowercase.
    ee_ncar_075 = models.CharField(max_length=1000,db_column='EE_NCAR_075', blank=True, null=True)  # Field name made lowercase.
    ee_ncar_086 = models.CharField(max_length=1000,db_column='EE_NCAR_086', blank=True, null=True)  # Field name made lowercase.
    ee_ncar_097 = models.CharField(max_length=1000,db_column='EE_NCAR_097', blank=True, null=True)  # Field name made lowercase.
    ee_ccch_076 = models.DecimalField(db_column='EE_CCCH_076', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_ccch_087 = models.DecimalField(db_column='EE_CCCH_087', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_ccch_098 = models.DecimalField(db_column='EE_CCCH_098', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_veco_099 = models.DecimalField(db_column='EE_VECO_099', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_cant_100 = models.DecimalField(db_column='EE_CANT_100', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_vebl_101 = models.DecimalField(db_column='EE_VEBL_101', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_cant_102 = models.DecimalField(db_column='EE_CANT_102', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_mar1_103 = models.CharField(max_length=1000,db_column='EE_MAR1_103', blank=True, null=True)  # Field name made lowercase.
    ee_mod1_104 = models.CharField(max_length=1000,db_column='EE_MOD1_104', blank=True, null=True)  # Field name made lowercase.
    ee_pla1_105 = models.CharField(max_length=1000,db_column='EE_PLA1_105', blank=True, null=True)  # Field name made lowercase.
    ee_ent1_106 = models.CharField(max_length=1000,db_column='EE_ENT1_106', blank=True, null=True)  # Field name made lowercase.
    ee_mar2_107 = models.CharField(max_length=1000,db_column='EE_MAR2_107', blank=True, null=True)  # Field name made lowercase.
    ee_mod2_108 = models.CharField(max_length=1000,db_column='EE_MOD2_108', blank=True, null=True)  # Field name made lowercase.
    ee_pla2_109 = models.CharField(max_length=1000,db_column='EE_PLA2_109', blank=True, null=True)  # Field name made lowercase.
    ee_ent2_110 = models.CharField(max_length=1000,db_column='EE_ENT2_110', blank=True, null=True)  # Field name made lowercase.
    ee_mar3_111 = models.CharField(max_length=1000,db_column='EE_MAR3_111', blank=True, null=True)  # Field name made lowercase.
    ee_mod3_112 = models.CharField(max_length=1000,db_column='EE_MOD3_112', blank=True, null=True)  # Field name made lowercase.
    ee_pla3_113 = models.CharField(max_length=1000,db_column='EE_PLA3_113', blank=True, null=True)  # Field name made lowercase.
    ee_ent3_114 = models.CharField(max_length=1000,db_column='EE_ENT3_114', blank=True, null=True)  # Field name made lowercase.
    ee_mar4_115 = models.CharField(max_length=1000,db_column='EE_MAR4_115', blank=True, null=True)  # Field name made lowercase.
    ee_mod4_116 = models.CharField(max_length=1000,db_column='EE_MOD4_116', blank=True, null=True)  # Field name made lowercase.
    ee_pla4_117 = models.CharField(max_length=1000,db_column='EE_PLA4_117', blank=True, null=True)  # Field name made lowercase.
    ee_ent4_118 = models.CharField(max_length=1000,db_column='EE_ENT4_118', blank=True, null=True)  # Field name made lowercase.
    ee_mar5_119 = models.CharField(max_length=1000,db_column='EE_MAR5_119', blank=True, null=True)  # Field name made lowercase.
    ee_mod5_120 = models.CharField(max_length=1000,db_column='EE_MOD5_120', blank=True, null=True)  # Field name made lowercase.
    ee_pla5_121 = models.CharField(max_length=1000,db_column='EE_PLA5_121', blank=True, null=True)  # Field name made lowercase.
    ee_ent5_122 = models.CharField(max_length=1000,db_column='EE_ENT5_122', blank=True, null=True)  # Field name made lowercase.
    ee_mar6_123 = models.CharField(max_length=1000,db_column='EE_MAR6_123', blank=True, null=True)  # Field name made lowercase.
    ee_mod6_124 = models.CharField(max_length=1000,db_column='EE_MOD6_124', blank=True, null=True)  # Field name made lowercase.
    ee_pla6_125 = models.CharField(max_length=1000,db_column='EE_PLA6_125', blank=True, null=True)  # Field name made lowercase.
    ee_ent6_126 = models.CharField(max_length=1000,db_column='EE_ENT6_126', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_escoltas'

#108
class IfEscoltas2(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    ee_frme_127 = models.CharField(max_length=1000,db_column='EE_FRME_127', blank=True, null=True)  # Field name made lowercase.
    ee_ctsp_128 = models.DecimalField(db_column='EE_CTSP_128', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_expl_132 = models.CharField(max_length=1000,db_column='EE_EXPL_132', blank=True, null=True)  # Field name made lowercase.
    ee_aees_133 = models.DecimalField(db_column='EE_AEES_133', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_expl_134 = models.CharField(max_length=1000,db_column='EE_EXPL_134', blank=True, null=True)  # Field name made lowercase.
    ee_crep_135 = models.CharField(max_length=1000,db_column='EE_CREP_135', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_escoltas_2'

#109
class IfEscoltas3(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    ee_pccr_136 = models.DecimalField(db_column='EE_PCCR_136', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_vier_137 = models.CharField(max_length=1000,db_column='EE_VIER_137', blank=True, null=True)  # Field name made lowercase.
    ee_cdsr_138 = models.DecimalField(db_column='EE_CDSR_138', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_expl_0139 = models.CharField(max_length=1000,db_column='EE_EXPL_0139', blank=True, null=True)  # Field name made lowercase.
    ee_pias_140 = models.DecimalField(db_column='EE_PIAS_140', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_caei_141 = models.CharField(max_length=1000,db_column='EE_CAEI_141', blank=True, null=True)  # Field name made lowercase.
    ee_cade_142 = models.DecimalField(db_column='EE_CADE_142', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_cual_143 = models.CharField(max_length=1000,db_column='EE_CUAL_143', blank=True, null=True)  # Field name made lowercase.
    ee_buep_144 = models.DecimalField(db_column='EE_BUEP_144', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_expl_145 = models.CharField(max_length=1000,db_column='EE_EXPL_145', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_escoltas_3'

#110
class IfEscoltas4(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    ee_cprt_146 = models.DecimalField(db_column='EE_CPRT_146', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_ccrc_147 = models.DecimalField(db_column='EE_CCRC_147', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_amep_148 = models.CharField(max_length=1000,db_column='EE_AMEP_148', blank=True, null=True)  # Field name made lowercase.
    ee_cpap_149 = models.DecimalField(db_column='EE_CPAP_149', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ee_cmtl_150 = models.CharField(max_length=1000,db_column='EE_CMTL_150', blank=True, null=True)  # Field name made lowercase.
    ee_obse_151 = models.CharField(max_length=1000,db_column='EE_OBSE_151', blank=True, null=True)  # Field name made lowercase.
    ee_noen_153 = models.CharField(max_length=1000,db_column='EE_NOEN_153', blank=True, null=True)  # Field name made lowercase.
    ee_naun_156 = models.CharField(max_length=1000,db_column='EE_NAUN_156', blank=True, null=True)  # Field name made lowercase.
    ee_dien_154 = models.CharField(max_length=1000,db_column='EE_DIEN_154', blank=True, null=True)  # Field name made lowercase.
    ee_dian_157 = models.CharField(max_length=1000,db_column='EE_DIAN_157', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_escoltas_4'

#111
class IfEstandar(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    es_ortr_007 = models.DecimalField(db_column='ES_ORTR_007', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    es_ream_021 = models.DecimalField(db_column='ES_REAM_021', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_ream_040 = models.CharField(max_length=1000,db_column='ES_REAM_040', blank=True, null=True)  # Field name made lowercase.
    es_inam_022 = models.DecimalField(db_column='ES_INAM_022', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_inam_041 = models.CharField(max_length=1000,db_column='ES_INAM_041', blank=True, null=True)  # Field name made lowercase.
    es_prac_023 = models.DecimalField(db_column='ES_PRAC_023', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_prac_042 = models.CharField(max_length=1000,db_column='ES_PRAC_042', blank=True, null=True)  # Field name made lowercase.
    es_caac_024 = models.DecimalField(db_column='ES_CAAC_024', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_caac_043 = models.CharField(max_length=1000,db_column='ES_CAAC_043', blank=True, null=True)  # Field name made lowercase.
    es_inac_025 = models.DecimalField(db_column='ES_INAC_025', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_inac_044 = models.CharField(max_length=1000,db_column='ES_INAC_044', blank=True, null=True)  # Field name made lowercase.
    es_inma_026 = models.DecimalField(db_column='ES_INMA_026', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_inma_045 = models.CharField(max_length=1000,db_column='ES_INMA_045', blank=True, null=True)  # Field name made lowercase.
    es_suto_059 = models.DecimalField(db_column='ES_SUTO_059', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_cond_027 = models.DecimalField(db_column='ES_COND_027', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_cond_046 = models.CharField(max_length=1000,db_column='ES_COND_046', blank=True, null=True)  # Field name made lowercase.
    es_fadi_028 = models.DecimalField(db_column='ES_FADI_028', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_fadi_047 = models.CharField(max_length=1000,db_column='ES_FADI_047', blank=True, null=True)  # Field name made lowercase.
    es_perf_029 = models.DecimalField(db_column='ES_PERF_029', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_perf_048 = models.CharField(max_length=1000,db_column='ES_PERF_048', blank=True, null=True)  # Field name made lowercase.
    es_anpe_030 = models.DecimalField(db_column='ES_ANPE_030', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_anpe_049 = models.CharField(max_length=1000,db_column='ES_ANPE_049', blank=True, null=True)  # Field name made lowercase.
    es_anco_031 = models.DecimalField(db_column='ES_ANCO_031', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_anco_050 = models.CharField(max_length=1000,db_column='ES_ANCO_050', blank=True, null=True)  # Field name made lowercase.
    es_riaf_032 = models.DecimalField(db_column='ES_RIAF_032', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_riaf_051 = models.CharField(max_length=1000,db_column='ES_RIAF_051', blank=True, null=True)  # Field name made lowercase.
    es_subt_060 = models.DecimalField(db_column='ES_SUBT_060', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_coco_033 = models.DecimalField(db_column='ES_COCO_033', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_coco_052 = models.CharField(max_length=1000,db_column='ES_COCO_052', blank=True, null=True)  # Field name made lowercase.
    es_pesi_034 = models.DecimalField(db_column='ES_PESI_034', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_pesi_053 = models.CharField(max_length=1000,db_column='ES_PESI_053', blank=True, null=True)  # Field name made lowercase.
    es_vure_035 = models.DecimalField(db_column='ES_VURE_035', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_vure_054 = models.CharField(max_length=1000,db_column='ES_VURE_054', blank=True, null=True)  # Field name made lowercase.
    es_vude_036 = models.DecimalField(db_column='ES_VUDE_036', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_vude_055 = models.CharField(max_length=1000,db_column='ES_VUDE_055', blank=True, null=True)  # Field name made lowercase.
    es_vuso_037 = models.DecimalField(db_column='ES_VUSO_037', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_vuso_056 = models.CharField(max_length=1000,db_column='ES_VUSO_056', blank=True, null=True)  # Field name made lowercase.
    es_vude_038 = models.DecimalField(db_column='ES_VUDE_038', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_vude_057 = models.CharField(max_length=1000,db_column='ES_VUDE_057', blank=True, null=True)  # Field name made lowercase.
    es_vuma_039 = models.DecimalField(db_column='ES_VUMA_039', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    es_vuma_058 = models.CharField(max_length=1000,db_column='ES_VUMA_058', blank=True, null=True)  # Field name made lowercase.
    es_subt_061 = models.DecimalField(db_column='ES_SUBT_061', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_estandar'

#112
class IfGvp(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    gvp_condvulne = models.CharField(max_length=1000,db_column='GVP_CONDVULNE', blank=True, null=True)  # Field name made lowercase.
    gvp_obs_sidh = models.CharField(max_length=1000,db_column='GVP_OBS_SIDH', blank=True, null=True)  # Field name made lowercase.
    gvp_inse_riesgo = models.CharField(max_length=1000,db_column='GVP_INSE_RIESGO', blank=True, null=True)  # Field name made lowercase.
    gvp_orden_publico = models.CharField(max_length=1000,db_column='GVP_ORDEN_PUBLICO', blank=True, null=True)  # Field name made lowercase.
    gvp_nivel_riesgo = models.IntegerField(db_column='GVP_NIVEL_RIESGO', blank=True, null=True)  # Field name made lowercase.
    gvp_obser_ciat = models.CharField(max_length=1000,db_column='GVP_OBSER_CIAT', blank=True, null=True)  # Field name made lowercase.
    gvp_eval_riesgo = models.CharField(max_length=1000,db_column='GVP_EVAL_RIESGO', blank=True, null=True)  # Field name made lowercase.
    gvp_med_emergencia = models.CharField(max_length=1000,db_column='GVP_MED_EMERGENCIA', blank=True, null=True)  # Field name made lowercase.
    gvp_med_proteccion = models.CharField(max_length=1000,db_column='GVP_MED_PROTECCION', blank=True, null=True)  # Field name made lowercase.
    gvp_medio_logis = models.CharField(max_length=1000,db_column='GVP_MEDIO_LOGIS', blank=True, null=True)  # Field name made lowercase.
    gvp_pondera_matriz = models.DecimalField(db_column='GVP_PONDERA_MATRIZ', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gvp_agenda_dia = models.IntegerField(db_column='GVP_AGENDA_DIA', blank=True, null=True)  # Field name made lowercase.
    gvp_agenda_mes = models.IntegerField(db_column='GVP_AGENDA_MES', blank=True, null=True)  # Field name made lowercase.
    gvp_agenda_agno = models.IntegerField(db_column='GVP_AGENDA_AGNO', blank=True, null=True)  # Field name made lowercase.
    gvp_analis_nombre = models.CharField(max_length=1000,db_column='GVP_ANALIS_NOMBRE', blank=True, null=True)  # Field name made lowercase.
    gvp_analis_cc = models.CharField(max_length=1000,db_column='GVP_ANALIS_CC', blank=True, null=True)  # Field name made lowercase.
    gvp_inse_riesgo_00 = models.CharField(max_length=1000,db_column='GVP_INSE_RIESGO_00', blank=True, null=True)  # Field name made lowercase.
    gvp_hecho_homicidio = models.CharField(max_length=1000,db_column='Gvp_hecho_homicidio', blank=True, null=True)  # Field name made lowercase.
    gvp_hecho_dh = models.CharField(max_length=1000,db_column='Gvp_hecho_dh', blank=True, null=True)  # Field name made lowercase.
    gvp_hecho_violacion = models.CharField(max_length=1000,db_column='Gvp_hecho_violacion', blank=True, null=True)  # Field name made lowercase.
    gvp_hecho_desplazamiento = models.CharField(max_length=1000,db_column='Gvp_hecho_desplazamiento', blank=True, null=True)  # Field name made lowercase.
    gvp_hecho_secuestro = models.CharField(max_length=1000,db_column='Gvp_hecho_secuestro', blank=True, null=True)  # Field name made lowercase.
    gvp_hecho_tortura = models.CharField(max_length=1000,db_column='Gvp_hecho_tortura', blank=True, null=True)  # Field name made lowercase.
    gvp_hecho_minas = models.CharField(max_length=1000,db_column='Gvp_hecho_minas', blank=True, null=True)  # Field name made lowercase.
    gvp_hecho_reclutamiento = models.CharField(max_length=1000,db_column='Gvp_hecho_reclutamiento', blank=True, null=True)  # Field name made lowercase.
    gvp_hecho_otros = models.CharField(max_length=1000,db_column='Gvp_hecho_otros', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_gvp'

#113
class IfHisHitoriagvp(models.Model):
    if_his_id = models.IntegerField(primary_key=True)
    if_his_orden_trabajo = models.CharField(max_length=1000,blank=True, null=True)
    if_his_solicitante = models.CharField(max_length=1000,blank=True, null=True)
    if_his_motivacionevnir = models.CharField(max_length=1000,db_column='if_his_motivacionEVNIR', blank=True, null=True)  # Field name made lowercase.
    if_his_nombres = models.CharField(max_length=1000,blank=True, null=True)
    if_his_apellidos = models.CharField(max_length=1000,blank=True, null=True)
    if_his_genero = models.CharField(max_length=1000,blank=True, null=True)
    if_his_cargos = models.CharField(max_length=1000,blank=True, null=True)
    if_his_fac_riesgo = models.CharField(max_length=1000,blank=True, null=True)
    if_his_tipoid = models.CharField(max_length=1000,db_column='if_his_tipoID', blank=True, null=True)  # Field name made lowercase.
    if_his_documento = models.CharField(max_length=1000,blank=True, null=True)
    if_his_academico = models.CharField(max_length=1000,blank=True, null=True)
    if_his_grupopob = models.CharField(max_length=1000,blank=True, null=True)
    if_his_analista = models.CharField(max_length=1000,blank=True, null=True)
    if_his_docanalista = models.CharField(max_length=1000,blank=True, null=True)
    if_his_entidad = models.CharField(max_length=1000,blank=True, null=True)
    if_his_analistacalidad = models.CharField(max_length=1000,blank=True, null=True)
    if_his_matriz = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    if_his_gvp = models.CharField(max_length=1000,blank=True, null=True)
    if_his_gvpanterior = models.CharField(max_length=1000,blank=True, null=True)
    if_his_proteccion = models.CharField(max_length=1000,blank=True, null=True)
    if_his_motivodev = models.CharField(max_length=1000,blank=True, null=True)
    if_his_estadocivil = models.CharField(max_length=1000,blank=True, null=True)
    if_his_ocupa_conyugue = models.CharField(max_length=1000,blank=True, null=True)
    if_his_cant_personas = models.CharField(max_length=1000,blank=True, null=True)
    if_his_ocupa_personas = models.CharField(max_length=1000,blank=True, null=True)
    if_his_muni = models.CharField(max_length=1000,blank=True, null=True)
    if_his_depto = models.CharField(max_length=1000,blank=True, null=True)
    if_his_alertas = models.CharField(max_length=1000,blank=True, null=True)
    if_his_direccion = models.CharField(max_length=1000,blank=True, null=True)
    if_his_antecedentes_pob = models.CharField(max_length=1000,blank=True, null=True)
    if_his_nrmunicipio = models.CharField(max_length=1000,db_column='if_his_NRMunicipio', blank=True, null=True)  # Field name made lowercase.
    if_his_lugarfechariesgo = models.CharField(max_length=1000,blank=True, null=True)
    if_his_contextoopregion = models.TextField(db_column='if_his_contextoOPregion', blank=True, null=True)  # Field name made lowercase.
    if_his_seguridadactual = models.CharField(max_length=1000,blank=True, null=True)
    if_his_med_proteccion = models.CharField(max_length=1000,blank=True, null=True)
    if_his_med_logistico = models.CharField(max_length=1000,blank=True, null=True)
    if_his_proceso_reevaluacion = models.CharField(max_length=1000,blank=True, null=True)
    if_his_fecha_entrevista = models.CharField(max_length=1000,blank=True, null=True)
    if_his_lugar_entrevistas = models.TextField(blank=True, null=True)
    if_his_contextualizacion = models.CharField(max_length=1000,blank=True, null=True)
    if_his_cruceinformacion = models.CharField(max_length=1000,blank=True, null=True)
    if_his_analisisinf = models.CharField(max_length=1000,blank=True, null=True)
    if_his_requerimiento_eval = models.CharField(max_length=1000,blank=True, null=True)
    if_his_decisiongvp = models.CharField(max_length=1000,blank=True, null=True)
    if_his_conceptogvp = models.CharField(max_length=1000,blank=True, null=True)
    if_his_delunp = models.CharField(max_length=1000,db_column='if_his_DelUNP', blank=True, null=True)  # Field name made lowercase.
    if_his_delmindef = models.CharField(max_length=1000,db_column='if_his_DelMindef', blank=True, null=True)  # Field name made lowercase.
    if_his_delponal = models.CharField(max_length=1000,db_column='if_his_DelPonal', blank=True, null=True)  # Field name made lowercase.
    if_his_delpres = models.CharField(max_length=1000,db_column='if_his_DelPres', blank=True, null=True)  # Field name made lowercase.
    if_his_deluaearv_dps = models.CharField(max_length=1000,db_column='if_his_DelUAEARV_DPS', blank=True, null=True)  # Field name made lowercase.
    if_his_oficio = models.CharField(max_length=1000,blank=True, null=True)
    if_his_actasesion = models.CharField(max_length=1000,blank=True, null=True)
    if_his_fechaactagvp = models.CharField(max_length=1000,db_column='if_his_fechaactaGVP', blank=True, null=True)  # Field name made lowercase.
    if_his_enalcepob = models.CharField(max_length=1000,blank=True, null=True)
    if_his_agno = models.CharField(max_length=1000,blank=True, null=True)
    if_his_unidad = models.CharField(max_length=1000,blank=True, null=True)
    if_his_mes = models.CharField(max_length=1000,blank=True, null=True)
    if_his_fecha_agenda = models.CharField(max_length=1000,blank=True, null=True)
    if_his_observaciones = models.CharField(max_length=1000,blank=True, null=True)
    if_his_fecha_notifica = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'if_his_hitoriagvp'

#114
class IfMedemerGrilla(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    em_inpe_073 = models.DecimalField(db_column='EM_INPE_073', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    em_medi_063 = models.CharField(max_length=1000,db_column='EM_MEDI_063', blank=True, null=True)  # Field name made lowercase.
    em_cant_064 = models.CharField(max_length=1000,db_column='EM_CANT_064', blank=True, null=True)  # Field name made lowercase.
    em_desc_065 = models.CharField(max_length=1000,db_column='EM_DESC_065', blank=True, null=True)  # Field name made lowercase.
    em_just_066 = models.CharField(max_length=1000,db_column='EM_JUST_066', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_medemer_grilla'

#115
class IfMedemerGrilla2(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    em_inpa_074 = models.DecimalField(db_column='EM_INPA_074', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    em_medi_069 = models.CharField(max_length=1000,db_column='EM_MEDI_069', blank=True, null=True)  # Field name made lowercase.
    em_cant_070 = models.DecimalField(db_column='EM_CANT_070', max_digits=25, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    em_desc_071 = models.CharField(max_length=1000,db_column='EM_DESC_071', blank=True, null=True)  # Field name made lowercase.
    em_just_072 = models.CharField(max_length=1000,db_column='EM_JUST_072', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_medemer_grilla2'

#116
class IfMedemergencia(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    em_ortr_007 = models.DecimalField(db_column='EM_ORTR_007', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    em_diso_061 = models.DecimalField(db_column='EM_DISO_061', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    em_obse_062 = models.CharField(max_length=1000,db_column='EM_OBSE_062', blank=True, null=True)  # Field name made lowercase.
    em_nofu_067 = models.CharField(max_length=1000,db_column='EM_NOFU_067', blank=True, null=True)  # Field name made lowercase.
    em_cafu_068 = models.CharField(max_length=1000,db_column='EM_CAFU_068', blank=True, null=True)  # Field name made lowercase.
    em_osad_075 = models.CharField(max_length=1000,db_column='EM_OSAD_075', blank=True, null=True)  # Field name made lowercase.
    em_noap_076 = models.CharField(max_length=1000,db_column='EM_NOAP_076', blank=True, null=True)  # Field name made lowercase.
    em_cafu_077 = models.CharField(max_length=1000,db_column='EM_CAFU_077', blank=True, null=True)  # Field name made lowercase.
    em_dcfun_078 = models.CharField(max_length=1000,db_column='EM_DCFUN_078', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_medemergencia'

#117
class IfMrecMemo(models.Model):
    if_mrec_secue = models.AutoField(primary_key=True)  # The composite primary key (if_mrec_secue, if_mrec_nromemo) found, that is not supported. The first column is selected.
    if_mrec_nromemo = models.CharField(max_length=1000)
    if_mrec_fechamemo = models.DateField(blank=True, null=True)
    if_mrec_elaboramemo = models.CharField(max_length=1000,blank=True, null=True)
    if_mrec_fecharecepcion = models.DateField(blank=True, null=True)
    if_mrec_nrofolios = models.IntegerField(blank=True, null=True)
    if_mrec_remitente = models.CharField(max_length=1000,blank=True, null=True)
    if_mrec_observacion = models.CharField(max_length=1000,blank=True, null=True)
    if_mrec_estado = models.IntegerField(blank=True, null=True)
    if_mrec_fecharecibo = models.DateField(blank=True, null=True)
    if_mrec_devolucion = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    if_mrec_fecha_memo_devol = models.DateField(blank=True, null=True)
    if_mrec_nro_memo_devol = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'if_mrec_memo'
        unique_together = (('if_mrec_secue', 'if_mrec_nromemo'),)

#118
class IfPrevencion(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    pr_ortr_007 = models.DecimalField(db_column='PR_ORTR_007', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pr_evas_061 = models.DecimalField(db_column='PR_EVAS_061', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pr_pras_062 = models.DecimalField(db_column='PR_PRAS_062', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pr_prim_063 = models.DecimalField(db_column='PR_PRIM_063', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pr_ocas_077 = models.CharField(max_length=1000,db_column='PR_OCAS_077', blank=True, null=True)  # Field name made lowercase.
    pr_paas_065 = models.DecimalField(db_column='PR_PAAS_065', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pr_paim_066 = models.DecimalField(db_column='PR_PAIM_066', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pr_opas_078 = models.CharField(max_length=1000,db_column='PR_OPAS_078', blank=True, null=True)  # Field name made lowercase.
    pr_rpas_068 = models.DecimalField(db_column='PR_RPAS_068', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pr_rpim_069 = models.DecimalField(db_column='PR_RPIM_069', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pr_oras_079 = models.CharField(max_length=1000,db_column='PR_ORAS_079', blank=True, null=True)  # Field name made lowercase.
    pr_otas_071 = models.DecimalField(db_column='PR_OTAS_071', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pr_otim_072 = models.DecimalField(db_column='PR_OTIM_072', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pr_ooas_080 = models.CharField(max_length=1000,db_column='PR_OOAS_080', blank=True, null=True)  # Field name made lowercase.
    pr_cuas_074 = models.CharField(max_length=1000,db_column='PR_CUAS_074', blank=True, null=True)  # Field name made lowercase.
    pr_cuim_075 = models.CharField(max_length=1000,db_column='PR_CUIM_075', blank=True, null=True)  # Field name made lowercase.
    pr_ocas_081 = models.CharField(max_length=1000,db_column='PR_OCAS_081', blank=True, null=True)  # Field name made lowercase.
    pr_prre_064 = models.DecimalField(db_column='PR_PRRE_064', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pr_ocre_082 = models.CharField(max_length=1000,db_column='PR_OCRE_082', blank=True, null=True)  # Field name made lowercase.
    pr_pare_067 = models.DecimalField(db_column='PR_PARE_067', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pr_opre_083 = models.CharField(max_length=1000,db_column='PR_OPRE_083', blank=True, null=True)  # Field name made lowercase.
    pr_rpre_070 = models.DecimalField(db_column='PR_RPRE_070', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pr_orre_084 = models.CharField(max_length=1000,db_column='PR_ORRE_084', blank=True, null=True)  # Field name made lowercase.
    pr_otre_073 = models.DecimalField(db_column='PR_OTRE_073', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pr_oore_085 = models.CharField(max_length=1000,db_column='PR_OORE_085', blank=True, null=True)  # Field name made lowercase.
    pr_cure_076 = models.CharField(max_length=1000,db_column='PR_CURE_076', blank=True, null=True)  # Field name made lowercase.
    pr_ocre_086 = models.CharField(max_length=1000,db_column='PR_OCRE_086', blank=True, null=True)  # Field name made lowercase.
    pr_nofu_087 = models.CharField(max_length=1000,db_column='PR_NOFU_087', blank=True, null=True)  # Field name made lowercase.
    pr_cafu_088 = models.CharField(max_length=1000,db_column='PR_CAFU_088', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_prevencion'

#119
class IfRepartoGralPte1(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=30, decimal_places=6)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=30, decimal_places=6)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=30, decimal_places=6)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=30, decimal_places=6)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=30, decimal_places=6)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=30, decimal_places=6)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    re_diso_001 = models.DecimalField(db_column='RE_DISO_001', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_meso_002 = models.DecimalField(db_column='RE_MESO_002', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_anso_003 = models.DecimalField(db_column='RE_ANSO_003', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_hoso_087 = models.DecimalField(db_column='RE_HOSO_087', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_miso_088 = models.DecimalField(db_column='RE_MISO_088', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_deso_004 = models.DecimalField(db_column='RE_DESO_004', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_muso_005 = models.DecimalField(db_column='RE_MUSO_005', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_enso_006 = models.CharField(max_length=1000,db_column='RE_ENSO_006', blank=True, null=True)  # Field name made lowercase.
    re_ortr_009 = models.DecimalField(db_column='RE_ORTR_009', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_dire_008 = models.CharField(max_length=1000,db_column='RE_DIRE_008', blank=True, null=True)  # Field name made lowercase.
    re_dire_009 = models.DecimalField(db_column='RE_DIRE_009', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_mere_010 = models.DecimalField(db_column='RE_MERE_010', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_anre_011 = models.DecimalField(db_column='RE_ANRE_011', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_hore_089 = models.DecimalField(db_column='RE_HORE_089', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_mire_090 = models.DecimalField(db_column='RE_MIRE_090', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_tiev_015 = models.DecimalField(db_column='RE_TIEV_015', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_niev_016 = models.CharField(max_length=1000,db_column='RE_NIEV_016', blank=True, null=True)  # Field name made lowercase.
    re_seev_021 = models.DecimalField(db_column='RE_SEEV_021', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_pnev_017 = models.CharField(max_length=1000,db_column='RE_PNEV_017', blank=True, null=True)  # Field name made lowercase.
    re_snev_018 = models.CharField(max_length=1000,db_column='RE_SNEV_018', blank=True, null=True)  # Field name made lowercase.
    re_paev_019 = models.CharField(max_length=1000,db_column='RE_PAEV_019', blank=True, null=True)  # Field name made lowercase.
    re_saev_020 = models.CharField(max_length=1000,db_column='RE_SAEV_020', blank=True, null=True)  # Field name made lowercase.
    re_inot_091 = models.CharField(max_length=1000,db_column='RE_INOT_091', blank=True, null=True)  # Field name made lowercase.
    re_grpo_022 = models.DecimalField(db_column='RE_GRPO_022', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grdp_023 = models.DecimalField(db_column='RE_GRDP_023', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grvd_035 = models.DecimalField(db_column='RE_GRVD_035', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grdi_024 = models.DecimalField(db_column='RE_GRDI_024', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grsp_036 = models.DecimalField(db_column='RE_GRSP_036', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grco_025 = models.DecimalField(db_column='RE_GRCO_025', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_gres_037 = models.DecimalField(db_column='RE_GRES_037', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_gros_026 = models.DecimalField(db_column='RE_GROS_026', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grde_038 = models.DecimalField(db_column='RE_GRDE_038', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grsi_027 = models.DecimalField(db_column='RE_GRSI_027', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grup_039 = models.DecimalField(db_column='RE_GRUP_039', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grog_028 = models.DecimalField(db_column='RE_GROG_028', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grad_040 = models.DecimalField(db_column='RE_GRAD_040', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grge_029 = models.DecimalField(db_column='RE_GRGE_029', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grdo_041 = models.DecimalField(db_column='RE_GRDO_041', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grmm_030 = models.DecimalField(db_column='RE_GRMM_030', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_gros_042 = models.DecimalField(db_column='RE_GROS_042', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grtd_031 = models.DecimalField(db_column='RE_GRTD_031', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grda_043 = models.DecimalField(db_column='RE_GRDA_043', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grpd_032 = models.DecimalField(db_column='RE_GRPD_032', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grfd_044 = models.DecimalField(db_column='RE_GRFD_044', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grip_033 = models.DecimalField(db_column='RE_GRIP_033', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grcc_045 = models.DecimalField(db_column='RE_GRCC_045', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_cope_034 = models.DecimalField(db_column='RE_COPE_034', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_gres_046 = models.CharField(max_length=1000,db_column='RE_GRES_046', blank=True, null=True)  # Field name made lowercase.
    re_grob_047 = models.CharField(max_length=1000,db_column='RE_GROB_047', blank=True, null=True)  # Field name made lowercase.
    re_maca_048 = models.DecimalField(db_column='RE_MACA_048', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_pete_054 = models.DecimalField(db_column='RE_PETE_054', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_viud_049 = models.DecimalField(db_column='RE_VIUD_049', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_pedi_055 = models.DecimalField(db_column='RE_PEDI_055', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_gest_050 = models.DecimalField(db_column='RE_GEST_050', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_lgtb_056 = models.DecimalField(db_column='RE_LGTB_056', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_lact_051 = models.DecimalField(db_column='RE_LACT_051', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_afro_057 = models.DecimalField(db_column='RE_AFRO_057', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_mame_052 = models.DecimalField(db_column='RE_MAME_052', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_indi_058 = models.DecimalField(db_column='RE_INDI_058', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_home_053 = models.DecimalField(db_column='RE_HOME_053', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_nsnr_059 = models.DecimalField(db_column='RE_NSNR_059', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_obse_060 = models.CharField(max_length=1000,db_column='RE_OBSE_060', blank=True, null=True)  # Field name made lowercase.
    re_deri_061 = models.DecimalField(db_column='RE_DERI_061', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_muri_062 = models.DecimalField(db_column='RE_MURI_062', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_core_063 = models.CharField(max_length=1000,db_column='RE_CORE_063', blank=True, null=True)  # Field name made lowercase.
    re_veri_064 = models.CharField(max_length=1000,db_column='RE_VERI_064', blank=True, null=True)  # Field name made lowercase.
    re_dere_065 = models.DecimalField(db_column='RE_DERE_065', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_mure_066 = models.DecimalField(db_column='RE_MURE_066', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_dire_067 = models.CharField(max_length=1000,db_column='RE_DIRE_067', blank=True, null=True)  # Field name made lowercase.
    re_nopc_068 = models.CharField(max_length=1000,db_column='RE_NOPC_068', blank=True, null=True)  # Field name made lowercase.
    re_enpc_069 = models.CharField(max_length=1000,db_column='RE_ENPC_069', blank=True, null=True)  # Field name made lowercase.
    re_cepc_070 = models.CharField(max_length=1000,db_column='RE_CEPC_070', blank=True, null=True)  # Field name made lowercase.
    re_depc_071 = models.DecimalField(db_column='RE_DEPC_071', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_mupc_072 = models.DecimalField(db_column='RE_MUPC_072', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_dipc_073 = models.CharField(max_length=1000,db_column='RE_DIPC_073', blank=True, null=True)  # Field name made lowercase.
    re_teri_074 = models.DecimalField(db_column='RE_TERI_074', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_nufo_075 = models.DecimalField(db_column='RE_NUFO_075', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_tire_076 = models.DecimalField(db_column='RE_TIRE_076', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_tide_078 = models.DecimalField(db_column='RE_TIDE_078', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_tisp_077 = models.DecimalField(db_column='RE_TISP_077', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_tiot_079 = models.DecimalField(db_column='RE_TIOT_079', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_diot_012 = models.DecimalField(db_column='RE_DIOT_012', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_meot_013 = models.DecimalField(db_column='RE_MEOT_013', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_anot_014 = models.DecimalField(db_column='RE_ANOT_014', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_hoot_092 = models.DecimalField(db_column='RE_HOOT_092', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_miot_093 = models.DecimalField(db_column='RE_MIOT_093', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_sere_094 = models.DecimalField(db_column='RE_SERE_094', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_asno_083 = models.DecimalField(db_column='RE_ASNO_083', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_fuau_084 = models.DecimalField(db_column='RE_FUAU_084', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_elab_085 = models.CharField(max_length=1000,db_column='RE_ELAB_085', blank=True, null=True)  # Field name made lowercase.
    re_diau_086 = models.CharField(max_length=1000,db_column='RE_DIAU_086', blank=True, null=True)  # Field name made lowercase.
    re_coca_095 = models.CharField(max_length=1000,db_column='RE_COCA_095', blank=True, null=True)  # Field name made lowercase.
    re_noca_096 = models.CharField(max_length=1000,db_column='RE_NOCA_096', blank=True, null=True)  # Field name made lowercase.
    re_nomb_087 = models.CharField(max_length=1000,db_column='RE_NOMB_087', blank=True, null=True)  # Field name made lowercase.
    re_obse_088 = models.CharField(max_length=1000,db_column='RE_OBSE_088', blank=True, null=True)  # Field name made lowercase.
    re_categoria = models.DecimalField(db_column='RE_CATEGORIA', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_grpo_022_historico = models.DecimalField(db_column='RE_GRPO_022_HISTORICO', max_digits=30, decimal_places=6, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cuf_int_sispro = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'if_reparto_gral_pte1'

#120
class IfRepartoGralPte2(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    re_ortr_008 = models.DecimalField(db_column='RE_ORTR_008', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_anas_097 = models.DecimalField(db_column='RE_ANAS_097', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_coel_098 = models.CharField(max_length=1000,db_column='RE_COEL_098', blank=True, null=True)  # Field name made lowercase.
    re_aunp_089 = models.DecimalField(db_column='RE_AUNP_089', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_deot_090 = models.DecimalField(db_column='RE_DEOT_090', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_meot_091 = models.DecimalField(db_column='RE_MEOT_091', max_digits=20, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_aeot_092 = models.DecimalField(db_column='RE_AEOT_092', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_hoot_093 = models.DecimalField(db_column='RE_HOOT_093', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_miot_110 = models.DecimalField(db_column='RE_MIOT_110', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_dien_093 = models.CharField(max_length=1000,db_column='RE_DIEN_093', blank=True, null=True)  # Field name made lowercase.
    re_noel_094 = models.CharField(max_length=1000,db_column='RE_NOEL_094', blank=True, null=True)  # Field name made lowercase.
    re_obse_095 = models.CharField(max_length=1000,db_column='RE_OBSE_095', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_reparto_gral_pte2'

#121
class IfRepartoGralPte3(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    re_ortr_007 = models.DecimalField(db_column='RE_ORTR_007', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_coel_999 = models.CharField(max_length=1000,db_column='RE_COEL_999', blank=True, null=True)  # Field name made lowercase.
    re_acte_102 = models.DecimalField(db_column='RE_ACTE_102', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_obde_103 = models.CharField(max_length=1000,db_column='RE_OBDE_103', blank=True, null=True)  # Field name made lowercase.
    re_dira_096 = models.DecimalField(db_column='RE_DIRA_096', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_mera_097 = models.DecimalField(db_column='RE_MERA_097', max_digits=20, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_anra_098 = models.DecimalField(db_column='RE_ANRA_098', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_sere_099 = models.DecimalField(db_column='RE_SERE_099', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_dien_100 = models.CharField(max_length=1000,db_column='RE_DIEN_100', blank=True, null=True)  # Field name made lowercase.
    re_nomb_101 = models.CharField(max_length=1000,db_column='RE_NOMB_101', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_reparto_gral_pte3'

#122
class IfRepartoGralPte4(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    re_otnu_111 = models.DecimalField(db_column='RE_OTNU_111', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_core_112 = models.DecimalField(db_column='RE_CORE_112', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_naas_102 = models.DecimalField(db_column='RE_NAAS_102', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_dira_103 = models.DecimalField(db_column='RE_DIRA_103', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_mera_104 = models.DecimalField(db_column='RE_MERA_104', max_digits=20, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_anra_105 = models.DecimalField(db_column='RE_ANRA_105', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    re_dias_107 = models.CharField(max_length=1000,db_column='RE_DIAS_107', blank=True, null=True)  # Field name made lowercase.
    re_nore_108 = models.CharField(max_length=1000,db_column='RE_NORE_108', blank=True, null=True)  # Field name made lowercase.
    re_obre_109 = models.CharField(max_length=1000,db_column='RE_OBRE_109', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_reparto_gral_pte4'

#123
class IfTerceros(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    do_ortr_007 = models.DecimalField(db_column='DO_ORTR_007', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'if_terceros'

#124
class IfTercerosGrilla(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_nrofila = models.DecimalField(max_digits=6, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolicitud = models.DecimalField(db_column='pen_IdSolicitud', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_pestana = models.CharField(max_length=1000)
    pen_idgrilla = models.DecimalField(db_column='pen_idGrilla', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_secueusuario = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_nombreusuario = models.CharField(max_length=1000)
    pen_idcargue = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_idsolpadre = models.DecimalField(db_column='pen_idSolPadre', max_digits=12, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchcargue = models.DateField()
    en_inpe_041 = models.DecimalField(db_column='EN_INPE_041', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_dien_017 = models.DecimalField(db_column='EN_DIEN_017', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_meen_018 = models.DecimalField(db_column='EN_MEEN_018', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_anen_019 = models.DecimalField(db_column='EN_ANEN_019', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_enre_020 = models.DecimalField(db_column='EN_ENRE_020', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_deen_021 = models.DecimalField(db_column='EN_DEEN_021', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_muen_022 = models.DecimalField(db_column='EN_MUEN_022', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_ldre_023 = models.CharField(max_length=1000,db_column='EN_LDRE_023', blank=True, null=True)  # Field name made lowercase.
    en_znre_024 = models.DecimalField(db_column='EN_ZNRE_024', max_digits=5, decimal_places=5, blank=True, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    en_nuto_025 = models.CharField(max_length=1000,db_column='EN_NUTO_025', blank=True, null=True)  # Field name made lowercase.
    en_ntde_026 = models.CharField(max_length=1000,db_column='EN_NTDE_026', blank=True, null=True)  # Field name made lowercase.
    en_noen_027 = models.CharField(max_length=1000,db_column='EN_NOEN_027', blank=True, null=True)  # Field name made lowercase.
    en_dipe_028 = models.CharField(max_length=1000,db_column='EN_DIPE_028', blank=True, null=True)  # Field name made lowercase.
    en_escd_29 = models.CharField(max_length=1000,db_column='EN_ESCD_29', blank=True, null=True)  # Field name made lowercase.
    en_icrc_030 = models.CharField(max_length=1000,db_column='EN_ICRC_030', blank=True, null=True)  # Field name made lowercase.
    en_noen_037 = models.CharField(max_length=1000,db_column='EN_NOEN_037', blank=True, null=True)  # Field name made lowercase.
    en_naup_039 = models.CharField(max_length=1000,db_column='EN_NAUP_039', blank=True, null=True)  # Field name made lowercase.
    en_dien_038 = models.CharField(max_length=1000,db_column='EN_DIEN_038', blank=True, null=True)  # Field name made lowercase.
    en_dian_040 = models.CharField(max_length=1000,db_column='EN_DIAN_040', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'if_terceros_grilla'

#125
class IfcolActRegactividad(models.Model):
    idifcol_act_secue = models.BigAutoField(primary_key=True)
    ifcol_secue = models.IntegerField(blank=True, null=True)
    usu_cod = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_fechaact = models.DateField(blank=True, null=True)
    ifcol_act_responsable = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_depto = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_mun = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_dir = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_telefono = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_participantes = models.IntegerField(blank=True, null=True)
    ifcol_act_descripact = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_conclusiones = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_par_estado = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_par_tipoactividad = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_telefono02 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_telefono03 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_fuente = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_persona_contact = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_fechafin = models.DateField(blank=True, null=True)
    ifcol_act_hora_actividad = models.IntegerField(blank=True, null=True)
    ifcol_act_entidad = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_cargo_contacto = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_nombre_documento = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_act_notas = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_act_regactividad'

#126
class IfcolAnaAnalista(models.Model):
    ifcol_ana_secue = models.BigAutoField(primary_key=True)
    ifcol_ana_nroidentifica = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_nombre = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_par_cargo = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_par_profesion = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_par_estado = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_ana_analista'

#127
class IfcolAneReganexos(models.Model):
    ifcol_ane_secue = models.BigAutoField(primary_key=True)
    ifcol_secue = models.ForeignKey('IfcolRegistroPte01', models.DO_NOTHING, db_column='ifcol_secue', blank=True, null=True)
    ifcol_par_codanexo = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_par_sino = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_ane_incidencias = models.IntegerField(blank=True, null=True)
    ifcol_ane_observa = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_ane_reganexos'

#128
class IfcolAneprePreanexos(models.Model):
    ifcol_anepre_secue = models.BigAutoField(primary_key=True)
    ifcol_pre_secue = models.ForeignKey('IfcolPreRevision', models.DO_NOTHING, db_column='ifcol_pre_secue', blank=True, null=True)
    ifcol_par_codanexo = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_par_sino = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_anepre_incidencias = models.IntegerField(blank=True, null=True)
    ifcol_anepre_observa = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_anepre_preanexos'

#129
class IfcolAnsoAnalissolicitud(models.Model):
    ifcol_anso_secue = models.BigAutoField(primary_key=True)
    ifcol_ana_secue = models.ForeignKey(IfcolAnaAnalista, models.DO_NOTHING, db_column='ifcol_ana_secue', blank=True, null=True)
    ifcol_secue = models.ForeignKey('IfcolRegistroPte01', models.DO_NOTHING, db_column='ifcol_secue', blank=True, null=True)
    ifcol_anso_par_estado = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_anso_fchreg = models.DateField(blank=True, null=True)
    ifcol_anso_horreg = models.TimeField(blank=True, null=True)
    ifcol_anso_nota = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_anso_analissolicitud'

#130
class IfcolDetRegdetallePte02(models.Model):
    ifcol_det_secue = models.AutoField(primary_key=True)
    ifcol_secue = models.IntegerField(blank=True, null=True)
    usu_cod = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='usu_cod', blank=True, null=True)
    ifcol_det_integr_nombre = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_det_integr_apellido = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_det_par_tipdoc = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_det_integr_nroid = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_det_par_sexo = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_det_integr_fchnace = models.DateField(blank=True, null=True)
    ifcol_det_observacion = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_det_nrodoc = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_det_par_nivel_estudio = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_det_regdetalle_pte02'

#131
class IfcolDocDocumentos(models.Model):
    ifcol_doc_secue = models.BigAutoField(primary_key=True)
    ifcol_secue = models.ForeignKey('IfcolRegistroPte01', models.DO_NOTHING, db_column='ifcol_secue', blank=True, null=True)
    usu_cod = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='usu_cod', blank=True, null=True)
    ifcol_doc_documento = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_doc_path = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_doc_nota = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_doc_fecha = models.DateField(blank=True, null=True)
    ifcol_doc_hora = models.TimeField(blank=True, null=True)
    ifcol_doc_version = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_doc_par_documento = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_num_xt = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_fch_xt = models.DateField(blank=True, null=True)
    ifcol_pre_secue = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_doc_documentos'

#132
class IfcolEntEntrevistas(models.Model):
    ifcol_ent_secue = models.BigAutoField(primary_key=True)
    ifcol_secue = models.ForeignKey('IfcolRegistroPte01', models.DO_NOTHING, db_column='ifcol_secue', blank=True, null=True)
    ifcol_ent_nombres = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_ent_apellidos = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_ent_fchentre = models.DateField(blank=True, null=True)
    ifcol_ent_depto = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_ent_municipio = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_ent_corregimiento = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_ent_vereda = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_ent_dir = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_ent_par_genero = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_ent_par_zona = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_ent_decripcion = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_ent_relacion = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_ent_entidad = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_ent_cargo = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_ent_entrevistas'

#133
class IfcolFacDiferencial(models.Model):
    ifcol_fac_secue = models.BigAutoField(primary_key=True)
    ifcol_secue = models.ForeignKey('IfcolRegistroPte01', models.DO_NOTHING, db_column='ifcol_secue', blank=True, null=True)
    ifcol_fac_par_tipofactor = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_fac_par_item = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_fac_nroindividuos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_fac_diferencial'

#134
class IfcolHecVictimisan(models.Model):
    ifcol_hec_secue = models.BigAutoField(primary_key=True)
    ifcol_secue = models.ForeignKey('IfcolRegistroPte01', models.DO_NOTHING, db_column='ifcol_secue', blank=True, null=True)
    ifcol_hec_par_dirigido = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_hec_fchhechos = models.DateField(blank=True, null=True)
    ifcol_hec_zona_ruralurb = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_hec_par_depto = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_hec_par_municipio = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_hec_corregimiento = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_hec_vereda = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_hec_direccion = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_hec_par_autor = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_hec_par_forma = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_hec_par_causa = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_hec_heridos = models.IntegerField(blank=True, null=True)
    ifcol_hec_muertos = models.IntegerField(blank=True, null=True)
    ifcol_hec_estructura = models.IntegerField(blank=True, null=True)
    ifcol_hec_descripcion = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_hec_otro_ame_autor = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_hec_tipo = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_hec_victimisan'

#135
class IfcolLinTiempo(models.Model):
    ifcol_lin_secue = models.BigAutoField(primary_key=True)
    ifcol_secue = models.ForeignKey('IfcolRegistroPte01', models.DO_NOTHING, db_column='ifcol_secue', blank=True, null=True)
    usu_cod = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='usu_cod', blank=True, null=True)
    ifcol_colectivo_par_estado = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_lin_actividad = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_lin_fecha = models.DateField(blank=True, null=True)
    ifcol_lin_hora = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_lin_tiempo'

#136
class IfcolMatBase(models.Model):
    ifcol_mat_secue = models.BigAutoField(primary_key=True)
    ifcol_mat_par_tipo = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_mat_par_subtipo = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_mat_par_estado = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_mat_escala = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_mat_base'

#137
class IfcolMatrRegistro(models.Model):
    ifcol_matr_secue = models.BigAutoField(primary_key=True)
    ifcol_secue = models.ForeignKey('IfcolRegistroPte01', models.DO_NOTHING, db_column='ifcol_secue', blank=True, null=True)
    ifcol_matr_par_tipo = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_matr_par_subtipo = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_matr_vlr_absoluto = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ifcol_matr_vlr_ponderado = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ifcol_matr_fuente = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_matr_registro'

#138
class IfcolMediMedidas(models.Model):
    ifcol_medi_secue = models.BigAutoField(primary_key=True)
    ifcol_secue = models.BigIntegerField(blank=True, null=True)
    ifcol_medi_par_matriz = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_medi_par_tipomedida = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_medi_entidad = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_medi_descripcion = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_medi_duracion = models.DecimalField(max_digits=6, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'ifcol_medi_medidas'

#139
class IfcolPreRevision(models.Model):
    ifcol_pre_secue = models.BigAutoField(primary_key=True)
    usu_cod = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='usu_cod', blank=True, null=True)
    ifcol_fch_registro = models.DateField(blank=True, null=True)
    ifcol_hor_registro = models.TimeField(blank=True, null=True)
    ifcol_nombre_solicita = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_par_tipodoc = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_iddoc_solicita = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_mail_solicitante = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_tel01_solicitante = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_tel02_solicitante = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_tel03_solicitante = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_cont01_nombre = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_cont01_tel01 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_cont01_tel02 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_cont02_nombre = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_cont02_tel01 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_cont02_tel02 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_nombre = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_id = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_depto = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_mun = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_corregi = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_vereda = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_dir = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_mail = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_contacto = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_tel01 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_tel02 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_par_grupo_pobla = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_par_categoria = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_par_estado = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_pre_num_xt = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_pre_fch_xt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_pre_revision'

#140
class IfcolPregConfig(models.Model):
    ifcol_preg_secue = models.AutoField(primary_key=True)
    ifcol_preg_codigo = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_preg_par_modulo = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_preg_par_submod = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_preg_pregunta = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_preg_par_tipodato = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_preg_par_obligatorio = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_preg_par_estado = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_preg_par_listavalores = models.BigIntegerField(blank=True, null=True)
    ifcol_preg_descripcion = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_preg_config'

#141
class IfcolRegistroPte01(models.Model):
    ifcol_secue = models.BigAutoField(primary_key=True)
    ifcol_par_estado_sol = models.CharField(max_length=1000,blank=True, null=True)
    usu_cod_registro = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='usu_cod_registro', blank=True, null=True)
    ifcol_fch_registro = models.DateField(blank=True, null=True)
    ifcol_hor_registro = models.TimeField(blank=True, null=True)
    ifcol_pre_secue = models.ForeignKey(IfcolPreRevision, models.DO_NOTHING, db_column='ifcol_pre_secue', blank=True, null=True)
    ifcol_col_memosigob = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_fch_solicitud = models.DateField(blank=True, null=True)
    ifcol_hor_solicitud = models.TimeField(blank=True, null=True)
    ifcol_nombre_solicita = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_par_tipodoc = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_iddoc_solicita = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_depto_solicitante = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_mun_solicitante = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_corregimto_solicitante = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_vereda_solicitante = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_dir_solicitante = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_mail_solicitante = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_tel01_solicitante = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_tel02_solicitante = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_tel03_solicitante = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_cont01_nombre = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_cont01_tel01 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_cont01_tel02 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_cont02_nombre = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_cont02_tel01 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_cont02_tel02 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_nombre = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_id = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_depto = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_mun = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_corregi = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_vereda = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_dir = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_mail = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_contacto = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_tel01 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_tel02 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_par_grupo_pobla = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_par_categoria = models.CharField(max_length=1000,blank=True, null=True)
    if_col_par_subcategoria = models.CharField(max_length=1000,blank=True, null=True)
    if_col_descripcion = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_par_funcion = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_par_acredita = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_par_rururb = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_solicita_par_relacion = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_repre_pri_nombre = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_repre_seg_nombre = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_repre_pri_apellido = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_repre_seg_apellido = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_repre_par_tipodoc = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_repre_nrodoc = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_repre_fchnace = models.DateField(blank=True, null=True)
    ifcol_repre_mail = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_repre_telefono01 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_repre_telefono02 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_repre_telefono03 = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_consen_sino = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_consen_mail = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_consen_fecha = models.DateField(blank=True, null=True)
    ifcol_col_memofch = models.DateField(blank=True, null=True)
    ifcol_colectivo_par_remite = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_devol_par_motivo = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_devol_descripcion = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_colectivo_remite = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_num_xt = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_fch_xt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_registro_pte01'

#142
class IfcolRptaPregRsptas(models.Model):
    ifcol_rpta_secue = models.BigAutoField(primary_key=True)
    ifcol_preg_secue = models.ForeignKey(IfcolPregConfig, models.DO_NOTHING, db_column='ifcol_preg_secue', blank=True, null=True)
    ifcol_secue = models.ForeignKey(IfcolRegistroPte01, models.DO_NOTHING, db_column='ifcol_secue', blank=True, null=True)
    ifcol_rpta_vlrnumerico = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    ifcol_rpta_vlrtexto = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_rpta_vlrfecha = models.DateField(blank=True, null=True)
    ifcol_rpta_vlr_lista = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_rpta_vlr_depto = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_rpta_vlr_mun = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_rpta_nota = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_rpta_preg_rsptas'

#143
class IfcolSeddCaracteriza(models.Model):
    ifcol_sedd_secue = models.BigAutoField(primary_key=True)
    idifcol_sedr_secue = models.ForeignKey('IfcolSedrSedriesgo', models.DO_NOTHING, db_column='idifcol_sedr_secue', blank=True, null=True)
    ifcol_sedd_par_pregunta = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_sedd_par_sino = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_sedd_valor = models.IntegerField(blank=True, null=True)
    ifcol_sedd_observa = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_sedd_caracteriza'

#144
class IfcolSedrSedriesgo(models.Model):
    idifcol_sedr_secue = models.BigAutoField(primary_key=True)
    ifcol_secue = models.ForeignKey(IfcolRegistroPte01, models.DO_NOTHING, db_column='ifcol_secue', blank=True, null=True)
    ifcol_sedr_par_depto = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_sedr_par_mun = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_sedr_dir = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_sedr_nombre = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_sedr_corregimiento = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_sedr_vereda = models.CharField(max_length=1000,blank=True, null=True)
    ifcol_sedr_par_zona = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifcol_sedr_sedriesgo'

#145
class IfmemBenBeneficiarioV1(models.Model):
    ifmem_ben_secue = models.AutoField(primary_key=True)
    ifmem_sol_secue = models.ForeignKey('IfmemSolicitudV1', models.DO_NOTHING, db_column='ifmem_sol_secue', blank=True, null=True)
    ifmem_ben_par_tipdoc = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_ben_nrodocumento = models.BigIntegerField(blank=True, null=True)
    ifmem_ben_prinombre = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_ben_segnombre = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_ben_priapellido = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_ben_segapellido = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_ben_par_parentesco = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_ben_par_genero = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_ben_fchnace = models.DateField(blank=True, null=True)
    ifmem_ben_edad = models.DecimalField(max_digits=5, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'ifmem_ben_beneficiario_v1'

#146
class IfmemDocDocumentosV1(models.Model):
    ifmem_doc_secue = models.AutoField(primary_key=True)
    ifmem_sol_secue = models.ForeignKey('IfmemSolicitudV1', models.DO_NOTHING, db_column='ifmem_sol_secue', blank=True, null=True)
    usu_cod = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='usu_cod', blank=True, null=True)
    ifmem_doc_documento = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_doc_path = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_doc_nota = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_doc_fecha = models.DateField(blank=True, null=True)
    ifmem_doc_hora = models.TimeField(blank=True, null=True)
    ifmem_doc_version = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_doc_par_documento = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifmem_doc_documentos_v1'

#147
class IfmemEntEntidadesV1(models.Model):
    ifmem_ent_secue = models.AutoField(primary_key=True)
    ifmem_ent_nit = models.BigIntegerField(blank=True, null=True)
    ifmem_ent_nombre = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_ent_area = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_ent_par_tipo = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifmem_ent_entidades_v1'

#148
class IfmemLinTiempoV1(models.Model):
    ifmem_lin_secue = models.AutoField(primary_key=True)
    ifmem_sol_secue = models.ForeignKey('IfmemSolicitudV1', models.DO_NOTHING, db_column='ifmem_sol_secue', blank=True, null=True)
    usu_cod = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='usu_cod', blank=True, null=True)
    ifmem_solicita_par_estado = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_lin_actividad = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_lin_fecha = models.DateField(blank=True, null=True)
    ifmem_lin_hora = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifmem_lin_tiempo_v1'

#149
class IfmemMedMedidasV1(models.Model):
    ifmem_med_secue = models.AutoField(primary_key=True)
    ifmem_sol_secue = models.ForeignKey('IfmemSolicitudV1', models.DO_NOTHING, db_column='ifmem_sol_secue', blank=True, null=True)
    ifmem_med_par_medida = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_med_cantidad = models.DecimalField(max_digits=6, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ifmem_med_tiempo = models.DecimalField(max_digits=6, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ifmem_med_descripcion = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifmem_med_medidas_v1'

#150
class IfmemNotasCoordinadorV1(models.Model):
    ifmem_notas_secue = models.AutoField(primary_key=True)
    ifmem_sol_secue = models.ForeignKey('IfmemSolicitudV1', models.DO_NOTHING, db_column='ifmem_sol_secue', blank=True, null=True)
    ifmem_notas_observa = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_notas_fchreg = models.DateField(blank=True, null=True)
    ifmem_notas_par_tipo = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifmem_notas_coordinador_v1'

#151
class IfmemSolicitudV1(models.Model):
    ifmem_sol_secue = models.AutoField(primary_key=True)
    ifmem_solicita_nroid = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_solicita_par_estado = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_solicita_fchregistro = models.DateField(blank=True, null=True)
    ifmem_solicita_horregistro = models.TimeField(blank=True, null=True)
    ifmem_solicita_nromemo = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_solicita_fchmemo = models.DateField(blank=True, null=True)
    ifmem_solicita_fchsolicitud = models.DateField(blank=True, null=True)
    ifmem_solicita_fchtramite = models.DateField(blank=True, null=True)
    ifmem_solicita_par_arearemite = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_solicita_nombre = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_solicita_par_tipodoc = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_solicita_id = models.BigIntegerField(blank=True, null=True)
    ifmem_solicita_fchfirma_entrega = models.DateField(blank=True, null=True)
    ifmem_solicit_memfirma_entrega = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_solicita_fchfirma_recibo = models.DateField(blank=True, null=True)
    ifmem_grupo_poblacional = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_categoria = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_prinom = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_segnom = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_priape = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_segape = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_par_genero = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_par_tipodoc = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_nrodoc = models.BigIntegerField(blank=True, null=True)
    ifmem_benppal_telefono = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_correo = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_depto_res = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_mun_res = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_dir_residencia = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_ent_pertenece_benefi = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_ent_asigno_medidas = models.ForeignKey(IfmemEntEntidadesV1, models.DO_NOTHING, db_column='ifmem_ent_asigno_medidas', blank=True, null=True)
    ifmem_par_medidas_previas = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_medidas_previas_det = models.CharField(max_length=1000,blank=True, null=True)
    usu_cod_registra = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='usu_cod_registra', blank=True, null=True)
    usu_cod_asignado = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='usu_cod_asignado', related_name='ifmemsolicitudv1_usu_cod_asignado_set', blank=True, null=True)
    ifmem_par_tipocobertura = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_depto_nac = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_mun_nac = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_fchnace = models.DateField(blank=True, null=True)
    ifmem_benppal_par_estciv = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_nrohijos_menor = models.IntegerField(blank=True, null=True)
    ifmem_benppal_nrohijos_mayor = models.IntegerField(blank=True, null=True)
    ifmem_benppal_par_enfoque = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_par_subenfoq = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_solicita_par_auto = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_par_ocupacion = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_par_inminencia = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_grupo_poblacional_2 = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_entidad_encargada_field = models.IntegerField(db_column='ifmem_entidad_encargada___', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    ifmem_fchrecep_unp = models.DateField(blank=True, null=True)
    ifmem_med_fchimplmta = models.DateField(blank=True, null=True)
    ifmem_med_fchdecision = models.DateField(blank=True, null=True)
    ifmem_med_remitido_a = models.IntegerField(blank=True, null=True)
    ifmem_concepto = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_relato = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_med_tiempo = models.IntegerField(blank=True, null=True)
    ifmem_med_par_tiempo = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_med_fchaprobacion = models.DateField(blank=True, null=True)
    ifmem_solicita_par_devolucion = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_solicita_des_devolucion = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_remi_par_sino = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_remi_nromemo = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_remi_fchremision = models.DateField(blank=True, null=True)
    ifmem_solicita_mepre_fch = models.DateField(blank=True, null=True)
    ifmem_solicita_mepre_sino = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_solicita_mepre_memo = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_imple_fchent = models.DateField(blank=True, null=True)
    ifmem_imple_memoent = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_solicita_fiscalia_fch = models.DateField(blank=True, null=True)
    ifmem_solicita_fiscalia_sino = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_solicita_fiscalia_memo = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_solicita_par_cptopsicolo = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_benppal_ocupacion = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_ent_asig_med_nombre = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_solicita_cptopsicolo = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_edad = models.IntegerField(blank=True, null=True)
    ifmem_obsr = models.CharField(max_length=1000,blank=True, null=True)
    ifmem_obs_temporalidad = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ifmem_solicitud_v1'

#152
class LogModificaciones(models.Model):
    log_mod_secue = models.AutoField(primary_key=True)
    log_mod_fecha = models.DateField()
    log_mod_usu = models.DecimalField(max_digits=12, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    log_mod_solpadre = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    log_mod_descripcion = models.CharField(max_length=1000,blank=True, null=True)
    log_mod_tipo_novedad = models.CharField(max_length=1000,blank=True, null=True)
    log_mod_sintesis_anterior = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_modificaciones'

#153
class MdlModulo(models.Model):
    mdl_cod = models.CharField(max_length=1000,primary_key=True)
    mdl_nombre = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdl_modulo'

#154
class ModVersion(models.Model):
    mod_modulo = models.CharField(max_length=1000,primary_key=True)
    mod_version_actual = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mod_version'

#155
class Pbcatcol(models.Model):
    pbc_tnam = models.CharField(max_length=1000, primary_key=True)
    pbc_tid = models.IntegerField(blank=True, null=True)
    pbc_ownr = models.CharField(max_length=1000,)
    pbc_cnam = models.CharField(max_length=1000,)
    pbc_cid = models.SmallIntegerField(blank=True, null=True)
    pbc_labl = models.CharField(max_length=1000,blank=True, null=True)
    pbc_lpos = models.SmallIntegerField(blank=True, null=True)
    pbc_hdr = models.CharField(max_length=1000,blank=True, null=True)
    pbc_hpos = models.SmallIntegerField(blank=True, null=True)
    pbc_jtfy = models.SmallIntegerField(blank=True, null=True)
    pbc_mask = models.CharField(max_length=1000,blank=True, null=True)
    pbc_case = models.SmallIntegerField(blank=True, null=True)
    pbc_hght = models.SmallIntegerField(blank=True, null=True)
    pbc_wdth = models.SmallIntegerField(blank=True, null=True)
    pbc_ptrn = models.CharField(max_length=1000,blank=True, null=True)
    pbc_bmap = models.CharField(max_length=1000,blank=True, null=True)
    pbc_init = models.CharField(max_length=1000,blank=True, null=True)
    pbc_cmnt = models.CharField(max_length=1000,blank=True, null=True)
    pbc_edit = models.CharField(max_length=1000,blank=True, null=True)
    pbc_tag = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatcol'
        unique_together = (('pbc_tnam', 'pbc_ownr', 'pbc_cnam'),)

#156
class Pbcatedt(models.Model):
    pbe_name = models.CharField(max_length=1000)
    pbe_edit = models.CharField(max_length=1000,blank=True, null=True)
    pbe_type = models.SmallIntegerField(blank=True, null=True)
    pbe_cntr = models.IntegerField(blank=True, null=True)
    pbe_seqn = models.SmallIntegerField(primary_key=True)
    pbe_flag = models.IntegerField(blank=True, null=True)
    pbe_work = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatedt'
        unique_together = (('pbe_name', 'pbe_seqn'),)

#157
class Pbcatfmt(models.Model):
    pbf_name = models.CharField(max_length=1000,unique=True)
    pbf_frmt = models.CharField(max_length=1000,blank=True, null=True)
    pbf_type = models.SmallIntegerField(blank=True, null=True)
    pbf_cntr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatfmt'

#158
class Pbcattbl(models.Model):
    pbt_tnam = models.CharField(max_length=1000)
    pbt_tid = models.IntegerField(blank=True, null=True)
    pbt_ownr = models.CharField(max_length=1000)
    pbd_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbd_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbd_fitl = models.CharField(max_length=1000,blank=True, null=True)
    pbd_funl = models.CharField(max_length=1000,blank=True, null=True)
    pbd_fchr = models.SmallIntegerField(blank=True, null=True)
    pbd_fptc = models.SmallIntegerField(blank=True, null=True)
    pbd_ffce = models.CharField(max_length=1000,blank=True, null=True)
    pbh_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbh_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbh_fitl = models.CharField(max_length=1000,blank=True, null=True)
    pbh_funl = models.CharField(max_length=1000,blank=True, null=True)
    pbh_fchr = models.SmallIntegerField(blank=True, null=True)
    pbh_fptc = models.SmallIntegerField(blank=True, null=True)
    pbh_ffce = models.CharField(max_length=1000,blank=True, null=True)
    pbl_fhgt = models.SmallIntegerField(blank=True, null=True)
    pbl_fwgt = models.SmallIntegerField(blank=True, null=True)
    pbl_fitl = models.CharField(max_length=1000,blank=True, null=True)
    pbl_funl = models.CharField(max_length=1000,blank=True, null=True)
    pbl_fchr = models.SmallIntegerField(blank=True, null=True)
    pbl_fptc = models.SmallIntegerField(blank=True, null=True)
    pbl_ffce = models.CharField(max_length=1000,blank=True, null=True)
    pbt_cmnt = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcattbl'
        unique_together = (('pbt_tnam', 'pbt_ownr'),)

#159
class Pbcatvld(models.Model):
    pbv_name = models.CharField(max_length=1000,unique=True, primary_key=True)
    pbv_vald = models.CharField(max_length=1000,blank=True, null=True)
    pbv_type = models.SmallIntegerField(blank=True, null=True)
    pbv_cntr = models.IntegerField(blank=True, null=True)
    pbv_msg = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatvld'

#160
class PenGvpBase(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_dele_unp_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_defen_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_poli_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_presi_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_deladm_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_uppcc_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_invi_fiscal_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_invi_procura_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_invi_defensor_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_invi_ciat_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_otrosinvi_nomb = models.CharField(max_length=1000,db_column='pen_otrosInvi_nomb', blank=True, null=True)  # Field name made lowercase.
    pen_obs_generales = models.CharField(max_length=1000,blank=True, null=True)
    pen_desicion = models.CharField(max_length=1000,blank=True, null=True)
    pen_concepto = models.CharField(max_length=1000,blank=True, null=True)
    pen_sesion = models.IntegerField(blank=True, null=True)
    pen_dele_unp_voto = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_defen_voto = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_poli_voto = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_presi_voto = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_deladm_voto = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_uppcc_voto = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pen_gvp_base'

#161
class PenGvpSesion(models.Model):
    pen_idsecue = models.AutoField(primary_key=True)
    pen_idsolpadre = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    pen_fchagenda = models.DateField(blank=True, null=True)
    pen_sesion = models.IntegerField(blank=True, null=True)
    pen_matriz_ctrai = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    pen_turno = models.IntegerField(blank=True, null=True)
    pen_tipo_orden = models.CharField(max_length=1000,blank=True, null=True)
    pen_result_matriz = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    pen_revision_cetrai = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_unp_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_unp_obs = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_unp_voto = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_defen_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_defen_obs = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_defen_voto = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_poli_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_poli_obs = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_poli_voto = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_presi_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_presi_obs = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_presi_voto = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_deladm_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_deladm_obs = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_deladm_voto = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_uppcc_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_uppcc_obs = models.CharField(max_length=1000,blank=True, null=True)
    pen_dele_uppcc_voto = models.CharField(max_length=1000,blank=True, null=True)
    pen_invi_fiscal_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_invi_fiscal_obs = models.CharField(max_length=1000,blank=True, null=True)
    pen_invi_procura_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_invi_procura_obs = models.CharField(max_length=1000,blank=True, null=True)
    pen_invi_defensor_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_invi_defensor_obs = models.CharField(max_length=1000,blank=True, null=True)
    pen_invi_ciat_nomb = models.CharField(max_length=1000,blank=True, null=True)
    pen_invi_ciat_obs = models.CharField(max_length=1000,blank=True, null=True)
    pen_otrosinvi_nomb = models.CharField(max_length=1000,db_column='pen_otrosInvi_nomb', blank=True, null=True)  # Field name made lowercase.
    pen_otrosinvi_obs = models.CharField(max_length=1000,db_column='pen_otrosInvi_obs', blank=True, null=True)  # Field name made lowercase.
    pen_obs_generales = models.CharField(max_length=1000,blank=True, null=True)
    pen_nivel_riesgo = models.CharField(max_length=1000,blank=True, null=True)
    pen_desicion = models.CharField(max_length=1000,blank=True, null=True)
    pen_concepto = models.CharField(max_length=1000,blank=True, null=True)
    pen_fch_genera = models.DateField(blank=True, null=True)
    pen_estado = models.CharField(max_length=1000,blank=True, null=True)
    pen_nivel_decision = models.CharField(max_length=1000,blank=True, null=True)
    pen_ejecuta_prorroga = models.CharField(max_length=1000,blank=True, null=True)
    pen_gvp_origen = models.CharField(max_length=1000,blank=True, null=True)
    pen_gvp_observa_matriz_gvp = models.CharField(max_length=1000,blank=True, null=True)
    pen_estado_revision = models.CharField(max_length=1000,blank=True, null=True)
    pen_analista_telefono = models.CharField(max_length=1000,blank=True, null=True)
    pen_digitador_caso = models.CharField(max_length=1000,blank=True, null=True)
    pen_observa_caso_gvp = models.CharField(max_length=1000,blank=True, null=True)
    usu_cod_reg = models.CharField(max_length=1000,blank=True, null=True)
    pen_fch_cierre_gvp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pen_gvp_sesion'

#162
class PenReevEnlacepobla(models.Model):
    pen_reev_secue = models.AutoField(primary_key=True)
    usu_codigo = models.CharField(max_length=1000,blank=True, null=True)
    cuf_sol_secue = models.IntegerField(blank=True, null=True)
    pen_reev_fchcreacion = models.DateField(blank=True, null=True)
    pen_reev_horacreacion = models.TimeField(blank=True, null=True)
    pen_reev_fchestado = models.DateField(blank=True, null=True)
    pen_reev_horaestado = models.TimeField(blank=True, null=True)
    pen_reev_concepto = models.CharField(max_length=1000,blank=True, null=True)
    cuf_dran_estado = models.CharField(max_length=1000,blank=True, null=True)
    pen_reev_fchagenda = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pen_reev_enlacepobla'

#163
class PerPerfil(models.Model):
    per_cod = models.IntegerField(primary_key=True)
    per_nombre = models.CharField(max_length=1000,blank=True, null=True)
    per_tab_acc = models.CharField(max_length=1000,blank=True, null=True)
    per_sql_acc = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'per_perfil'

#164
class PqrAreAreas(models.Model):
    pqr_are_secue = models.AutoField(primary_key=True)
    pqr_are_nombre = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pqr_are_areas'

#165
class PqrEmpEmpresas(models.Model):
    pqr_emp_secue = models.AutoField(primary_key=True)
    pqr_emp_nit = models.CharField(max_length=1000,blank=True, null=True)
    pqr_emp_nombre = models.CharField(max_length=1000,blank=True, null=True)
    pqr_par_tipo_emp = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pqr_emp_empresas'

#166
class PqrPerPersonas(models.Model):
    pqr_per_secue = models.AutoField(primary_key=True)
    pqr_per_nombre1 = models.CharField(max_length=1000,blank=True, null=True)
    pqr_per_nombre2 = models.CharField(max_length=1000,blank=True, null=True)
    pqr_per_apellido1 = models.CharField(max_length=1000,blank=True, null=True)
    pqr_per_apellido2 = models.CharField(max_length=1000,blank=True, null=True)
    pqr_per_nroid = models.CharField(max_length=1000,blank=True, null=True)
    pqr_par_grupo = models.CharField(max_length=1000,blank=True, null=True)
    pqr_par_categoria = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_secue = models.ForeignKey('PqrRegRegistro', models.DO_NOTHING, db_column='pqr_reg_secue', blank=True, null=True)
    pqr_par_sexo = models.CharField(max_length=1000,blank=True, null=True)
    pqr_par_medida_vigente = models.CharField(max_length=1000,blank=True, null=True)
    pqr_per_ot = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'pqr_per_personas'

#167
class PqrRegRegistro(models.Model):
    pqr_reg_secue = models.AutoField(primary_key=True)
    pqr_reg_entradaext = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_enlaceext = models.CharField(max_length=1000,blank=True, null=True)
    pqr_par_tipo_ext = models.CharField(max_length=1000,blank=True, null=True)
    pqr_par_estado = models.CharField(max_length=1000,blank=True, null=True)
    pqr_par_devolucion = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_fchradica_unp = models.DateField(blank=True, null=True)
    pqr_reg_fchradica_ser = models.DateField(blank=True, null=True)
    pqr_reg_fchregistro = models.DateField(blank=True, null=True)
    pqr_reg_fchreparto = models.DateField(blank=True, null=True)
    pqr_reg_ot = models.IntegerField(blank=True, null=True)
    pqr_par_tipo_pqr = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_fchproy_entrega = models.DateField(blank=True, null=True)
    pqr_reg_fch_cierre = models.DateField(blank=True, null=True)
    usu_cod_registro = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='usu_cod_registro', blank=True, null=True)
    usu_cod_reparto = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='usu_cod_reparto', related_name='pqrregregistro_usu_cod_reparto_set', blank=True, null=True)
    usu_cod_tramita = models.ForeignKey('UsuUsuario', models.DO_NOTHING, db_column='usu_cod_tramita', related_name='pqrregregistro_usu_cod_tramita_set', blank=True, null=True)
    pqr_reg_salidaext = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_fchsalidaext = models.DateField(blank=True, null=True)
    pqr_par_estado_insumo = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_horas_espra_insumo = models.IntegerField(blank=True, null=True)
    pqr_reg_horas_real_respta = models.IntegerField(blank=True, null=True)
    pqr_reg_solucion = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_descripcion = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_items_rpta = models.IntegerField(blank=True, null=True)
    pqr_par_medio_rpta = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_rmte_nombre1 = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_rmte_nombre2 = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_rmte_apellido1 = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_rmte_apellido2 = models.CharField(max_length=1000,blank=True, null=True)
    pqr_par_rmte_tipodoc = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_rmte_nro_docto = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_rmte_dir_notifica = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_rmte_dep_notifica = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_rmte_mun_notifica = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_rmte_correo = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_grupo_poblacional = models.CharField(max_length=1000,blank=True, null=True)
    pqr_reg_categoria = models.CharField(max_length=1000,blank=True, null=True)
    pqr_par_rmte_medvigente = models.CharField(max_length=1000,blank=True, null=True)
    pqr_par_rmte_sexo = models.CharField(max_length=1000,blank=True, null=True)
    pqr_are_secue = models.ForeignKey(PqrAreAreas, models.DO_NOTHING, db_column='pqr_are_secue', blank=True, null=True)
    pqr_emp_secue = models.ForeignKey(PqrEmpEmpresas, models.DO_NOTHING, db_column='pqr_emp_secue', blank=True, null=True)
    pqr_reg_solicitante = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pqr_reg_registro'

#168
class PrgPrograma(models.Model):
    prg_cod = models.CharField(max_length=1000,primary_key=True)
    prg_descri = models.CharField(max_length=1000,blank=True, null=True)
    mdl_cod = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prg_programa'

#169
class PxpProgPerf(models.Model):
    secue = models.IntegerField(primary_key=True)
    prg_cod = models.CharField(max_length=1000,blank=True, null=True)
    per_cod = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pxp_prog_perf'

#170
class SecSecuencias(models.Model):
    sec_nombre = models.CharField(max_length=1000,primary_key=True)
    sec_secue = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'sec_secuencias'

#171
class UsuAcceso(models.Model):
    id_secue = models.AutoField(primary_key=True)
    usu_cod = models.CharField(max_length=1000,blank=True, null=True)
    fch_acceso = models.DateField(blank=True, null=True)
    hora_acceso = models.TimeField(blank=True, null=True)
    tipo_transaccion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usu_acceso'

#172
class UsuHistClave(models.Model):
    usu_hist_secue = models.AutoField(primary_key=True)
    usu_cod = models.CharField(max_length=1000,blank=True, null=True)
    usu_clave = models.CharField(max_length=1000,blank=True, null=True)
    usu_fch_clave = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usu_hist_clave'

#173
class UsuUsuario(models.Model):
    usu_cod = models.CharField(max_length=1000,primary_key=True)
    usu_nombre = models.CharField(max_length=1000,blank=True, null=True)
    usu_fcf_cr = models.DateField(blank=True, null=True)
    per_cod = models.IntegerField(blank=True, null=True)
    usu_privil = models.CharField(max_length=1000,blank=True, null=True)
    usu_estado = models.CharField(max_length=1000,blank=True, null=True)
    usu_clave = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usu_usuario'
