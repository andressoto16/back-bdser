from conexionbd.models import *
from rest_framework import serializers
from conexionbd.views import departamento, municipio, poblacionser, subpoblacion, tipoEstudio


#1
class apiAReeval(serializers.ModelSerializer):
    class Meta:
        model = AReeval
        fields = '__all__'
 
#12
class apiAccUsuUsuario(serializers.ModelSerializer):
    class Meta:
        model = AccUsuUsuario
        fields = '__all__'
        
#14
class apiCerActgGenera(serializers.ModelSerializer):
    class Meta:
        model = CerActgGenera
        fields = '__all__'
        
#16
class apiCerAgeAgenda(serializers.ModelSerializer):
    class Meta:
        model = CerAgeAgenda
        fields = '__all__'
        
#18
class apiCerCalCambioCalidad(serializers.ModelSerializer):
    class Meta:
        model = CerCalCambioCalidad
        fields = '__all__'
        
#19
class apiCerCerCerrem(serializers.ModelSerializer):
    class Meta:
        model = CerCerCerrem
        fields = '__all__'
        
#21
class apiCerDetMedida(serializers.ModelSerializer):
    class Meta:
        model = CerDetMedida
        fields = '__all__'
        
#22
class apiCerDetValoresIndCol(serializers.ModelSerializer):
    class Meta:
        model = CerDetValoresIndCol
        fields = '__all__'
        
#22
class apiCerEvaEvaluado(serializers.ModelSerializer):
    class Meta:
        model = CerEvaEvaluado
        fields = '__all__'
        
#31
class apiCerSeg2Comite(serializers.ModelSerializer):
    class Meta:
        model = CerSeg2Comite
        fields = '__all__'
        
#32
class apiCerSegComite(serializers.ModelSerializer):
    class Meta:
        model = CerSegComite
        fields = '__all__'
        
#40
class apiCufCarCargues(serializers.ModelSerializer):
    class Meta:
        model = CufCarCargues
        fields = '__all__'
        
#53
class apiCufForFormatos(serializers.ModelSerializer):
    class Meta:
        model = CufForFormatos
        fields = '__all__'
        
#69
class apiCufSolSolicitud(serializers.ModelSerializer):
    class Meta:
        model = CufSolSolicitud
        fields = '__all__'
        
#74
class apiIfActa(serializers.ModelSerializer):
    class Meta:
        model = IfActa
        fields = '__all__'
        
#74
class apiIfAnuAnulaot(serializers.ModelSerializer):
    class Meta:
        model = IfAnuAnulaot
        fields = '__all__'
        
#79
class apiIfConsentimiento(serializers.ModelSerializer):
    class Meta:
        model = IfConsentimiento
        fields = '__all__'
        
#81
class apiIfContactosGrilla(serializers.ModelSerializer):
    class Meta:
        model = IfContactosGrilla
        fields = '__all__'
        
#82
class apiIfCuerpo(serializers.ModelSerializer):
    class Meta:
        model = IfCuerpo
        fields = '__all__'
        
#83
class apiIfCuerpo2(serializers.ModelSerializer):
    class Meta:
        model = IfCuerpo2
        fields = '__all__'
        
#84
class apiIfCuerpo3(serializers.ModelSerializer):
    class Meta:
        model = IfCuerpo3
        fields = '__all__'
        
#85
class apiIfCuerpo4(serializers.ModelSerializer):
    class Meta:
        model = IfCuerpo4
        fields = '__all__'
        
#86
class apiIfCuerpo5(serializers.ModelSerializer):
    class Meta:
        model = IfCuerpo5
        fields = '__all__'
        
#87
class apiIfCuerpo6(serializers.ModelSerializer):
    class Meta:
        model = IfCuerpo6
        fields = '__all__'
        
#88
class apiIfCuerpo7(serializers.ModelSerializer):
    class Meta:
        model = IfCuerpo7
        fields = '__all__'
        
#89
class apiIfDesplazamiento(serializers.ModelSerializer):
    class Meta:
        model = IfDesplazamiento
        fields = '__all__'
        
#92
class apiIfDocumentalGrilla(serializers.ModelSerializer):
    class Meta:
        model = IfDocumentalGrilla
        fields = '__all__'
        
#94
class apiIfEntornos(serializers.ModelSerializer):
    class Meta:
        model = IfEntornos
        fields = '__all__'
        
#99
class apiIfEntrevista(serializers.ModelSerializer):
    class Meta:
        model = IfEntrevista
        fields = '__all__'
        
#100
class apiIfEntrevista2(serializers.ModelSerializer):
    class Meta:
        model = IfEntrevista2
        fields = '__all__'
        
class apiIfgvp(serializers.ModelSerializer):
    class Meta:
        model = IfGvp
        fields = '__all__'
        
class apiIfRepartoGralPte1(serializers.ModelSerializer):
    class Meta:
        model = IfRepartoGralPte1
        fields = '__all__'
        
class apiIfRepartoGralPte2(serializers.ModelSerializer):
    class Meta:
        model = CufSolSolicitud
        fields = '__all__'
            
class repartoPermiso(serializers.ModelSerializer):
    ordenTrabajo = serializers.SerializerMethodField()
    analistaRiesgo = serializers.SerializerMethodField()
    nombreEvaluado = serializers.SerializerMethodField()
    nuipEvaluado = serializers.SerializerMethodField()
    fechaAutorizacionOT = serializers.SerializerMethodField()
    poblacion = serializers.SerializerMethodField()
    subpoblacion = serializers.SerializerMethodField()
    tipoEstudio = serializers.SerializerMethodField()
    departamento = serializers.SerializerMethodField()
    municipio = serializers.SerializerMethodField()
    cargoEvaluado = serializers.SerializerMethodField()
    fechaEntrevista = serializers.SerializerMethodField()
    celularEvaluado = serializers.SerializerMethodField()
    correoElectronicoEvaluado = serializers.SerializerMethodField()
    desplazamientoEvaluado = serializers.SerializerMethodField()
    FactorDiferencialEvaluado = serializers.SerializerMethodField()
    sistesisHechos1 = serializers.SerializerMethodField()
    sistesisHechos2 = serializers.SerializerMethodField()
    contextoPublico = serializers.SerializerMethodField()
    observacionesCIAT = serializers.SerializerMethodField()
    evaluacionRiesgoAnteriol = serializers.SerializerMethodField()
    medidaEmergencia = serializers.SerializerMethodField()
    medidasProteccionVigente = serializers.SerializerMethodField()
    ponderacionMatriz = serializers.SerializerMethodField()
    
    # analista = 
    class Meta:
        model = IfRepartoGralPte1
        fields = ['ordenTrabajo','analistaRiesgo','nombreEvaluado','nuipEvaluado','fechaAutorizacionOT',
                  'poblacion','subpoblacion','tipoEstudio','departamento','municipio','cargoEvaluado','fechaEntrevista',
                  'celularEvaluado','correoElectronicoEvaluado','desplazamientoEvaluado','FactorDiferencialEvaluado',
                  'sistesisHechos1','sistesisHechos2', 'contextoPublico','observacionesCIAT','evaluacionRiesgoAnteriol',
                  'medidaEmergencia','medidasProteccionVigente','ponderacionMatriz']       
       
    def get_ordenTrabajo(self, obj):
        return int(obj.re_ortr_009) if obj and obj.re_ortr_009 is not None else None
    
    def get_analistaRiesgo(self, obj):
        analista = CufDranDetrangos.objects.filter(cuf_dran_valor = obj.re_asno_083).last()
        return  analista.cuf_dran_nombre if analista else None
       
    def get_nombreEvaluado(self, obj):
        primer_nombre = obj.re_pnev_017
        segundo_nombre = obj.re_snev_018
        primer_apellido = obj.re_paev_019
        segundo_apellido = obj.re_saev_020
        nombre_completo = ' '.join(filter(None, [primer_nombre, segundo_nombre,primer_apellido,segundo_apellido]))
        return nombre_completo if nombre_completo else None
    
    def get_nuipEvaluado(self, obj):
        return int(obj.re_niev_016) if obj and obj.re_niev_016 is not None else None
       
    def get_fechaAutorizacionOT(self, obj):
        dia = str(obj.re_diot_012)
        mes = str(obj.re_meot_013)
        ango = str(obj.re_anot_014)
        fecha_completa = '-'.join(filter(None, [ango,mes,dia]))
        return fecha_completa
    
    def get_poblacion(self, obj):
        return poblacionser(obj.re_grpo_022) if obj and obj.re_grpo_022 is not None else 'Población no encontrado'
        
    def get_subpoblacion(self, obj):
        return subpoblacion(obj.re_categoria) if obj and obj.re_categoria is not None else 'Subpoblación no encontrado'
        
    def get_tipoEstudio(self, obj):
        return tipoEstudio(obj.re_teri_074) if obj and obj.re_teri_074 is not None else 'Tipo de estudio no asignado'
        
    def get_departamento(self, obj):
        return departamento(obj.re_deso_004) if obj and obj.re_deso_004 is not None else 'Departamento no encontrado'
        
    def get_municipio(self, obj):
        return municipio(obj.re_muso_005) if obj and obj.re_muso_005 is not None else 'Municipio no encontrado'
        
    def get_cargoEvaluado(self, obj):
        entrevista = IfEntrevista2.objects.filter(pen_idsolpadre = obj.re_ortr_009).last()
        return entrevista.en_obgp_082 if entrevista else 'No específica cargo hasta el momento'
    
    def get_fechaEntrevista(self, obj):
        entrevista = IfEntrevista.objects.filter(en_ortr_001 = obj.re_ortr_009).last()
        dia = str(entrevista.en_dien_015) if entrevista and entrevista.en_dien_015 is not None else None
        mes = str(entrevista.en_meen_016) if entrevista and entrevista.en_meen_016 is not None else None
        agno = str(entrevista.en_anen_017) if entrevista and entrevista.en_anen_017 is not None else None
        fecha_completa = '-'.join(filter(None, [agno, mes, dia]))
        return fecha_completa if fecha_completa else 'Sin información'

    def get_celularEvaluado(self, obj):
        entrevista = IfEntrevista.objects.filter(en_ortr_001 = obj.re_ortr_009).last()
        return str(entrevista.en_tcre_046) if entrevista else 'Sin información'

    def get_correoElectronicoEvaluado(self, obj):
        entrevista = IfEntrevista.objects.filter(en_ortr_001 = obj.re_ortr_009).last()
        return str(entrevista.en_cere_047) if entrevista else 'Sin información'
    
    def get_desplazamientoEvaluado(self, obj):
        desplazamiento = IfDesplazamiento.objects.filter(de_ortr_001 = obj.re_ortr_009).last()
        return desplazamiento.de_tmco_050 if desplazamiento else 'Sin información'
        
    def get_FactorDiferencialEvaluado(self, obj):
        gvp = IfGvp.objects.filter(pen_idsolpadre = obj.re_ortr_009).last()
        return gvp.gvp_condvulne if gvp else 'Sin información'
    
    def get_sistesisHechos1(self, obj):
        gvp = IfGvp.objects.filter(pen_idsolpadre = obj.re_ortr_009).last()
        return gvp.gvp_inse_riesgo_00 if gvp else 'Sin información'
        
    def get_sistesisHechos2(self, obj):
        gvp = IfGvp.objects.filter(pen_idsolpadre = obj.re_ortr_009).last()
        return gvp.gvp_inse_riesgo if gvp else 'Sin información'
    
    def get_contextoPublico(self, obj):
        gvp = IfGvp.objects.filter(pen_idsolpadre = obj.re_ortr_009).last()
        return gvp.gvp_orden_publico if gvp else 'Sin información'
    
    def get_observacionesCIAT(self, obj):
        gvp = IfGvp.objects.filter(pen_idsolpadre = obj.re_ortr_009).last()
        return gvp.gvp_obser_ciat if gvp else 'Sin información'
    
    def get_evaluacionRiesgoAnteriol(self, obj):
        gvp = IfGvp.objects.filter(pen_idsolpadre = obj.re_ortr_009).last()
        return gvp.gvp_eval_riesgo if gvp else 'Sin información'
    
    def get_medidaEmergencia(self, obj):
        gvp = IfGvp.objects.filter(pen_idsolpadre = obj.re_ortr_009).last()
        return gvp.gvp_med_emergencia if gvp else 'Sin información'
    
    def get_medidasProteccionVigente(self, obj):
        gvp = IfGvp.objects.filter(pen_idsolpadre = obj.re_ortr_009).last()
        return gvp.gvp_med_proteccion if gvp else 'Sin información'
    
    def get_ponderacionMatriz(self, obj):
        gvp = IfGvp.objects.filter(pen_idsolpadre = obj.re_ortr_009).last()
        return gvp.gvp_pondera_matriz if gvp else 'Sin información'