from conexionbd.models import *
from rest_framework import serializers


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