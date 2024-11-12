from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from conexionbd.models import *
from conexionbd.serializer import *

#1
class AReevalPermiso(viewsets.ModelViewSet):
    queryset = AReeval.objects.all()
    serializer_class = apiAReeval
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cc']
    http_method_names = ['get']

#12    
class AccUsuUsuarioPermiso(viewsets.ModelViewSet):
    queryset = AccUsuUsuario.objects.all()
    serializer_class = apiAccUsuUsuario
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usu_cod','acc_usu_mail']
    http_method_names = ['get']

#14
class CerActgGeneraPermiso(viewsets.ModelViewSet):
    queryset = CerActgGenera.objects.all()[:500]
    serializer_class = apiCerActgGenera
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']

#16
class CerAgeAgendaPermiso(viewsets.ModelViewSet):
    queryset = CerAgeAgenda.objects.all()[:500]
    serializer_class = apiCerAgeAgenda
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#18
class CerCalCambioCalidadPermiso(viewsets.ModelViewSet):
    queryset = CerCalCambioCalidad.objects.all()[:500]
    serializer_class = apiCerCalCambioCalidad
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#19
class CerCerCerremPermiso(viewsets.ModelViewSet):
    queryset = CerCerCerrem.objects.all()[:500]
    serializer_class = apiCerCerCerrem
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#21
class CerDetMedidaPermiso(viewsets.ModelViewSet):
    queryset = CerDetMedida.objects.all()[:500]
    serializer_class = apiCerDetMedida
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#22
class CerDetValoresIndColPermiso(viewsets.ModelViewSet):
    queryset = CerDetValoresIndCol.objects.all()[:50]
    serializer_class = apiCerDetValoresIndCol
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#25
class CerEvaEvaluadoPermiso(viewsets.ModelViewSet):
    queryset = CerEvaEvaluado.objects.all()[:500]
    serializer_class = apiCerEvaEvaluado
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#31
class CerSeg2ComitePermiso(viewsets.ModelViewSet):
    queryset = CerSeg2Comite.objects.all()[:500]
    serializer_class = apiCerSeg2Comite
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#32
class CerSegComitePermiso(viewsets.ModelViewSet):
    queryset = CerSegComite.objects.all()[:500]
    serializer_class = apiCerSegComite
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#40
class CufCarCarguesPermiso(viewsets.ModelViewSet):
    queryset = CufCarCargues.objects.all()[:500]
    serializer_class = apiCufCarCargues
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#53
class CufForFormatosPermiso(viewsets.ModelViewSet):
    queryset = CufForFormatos.objects.all()[:500]
    serializer_class = apiCufForFormatos
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#69
class CufSolSolicitudPermiso(viewsets.ModelViewSet):
    queryset = CufSolSolicitud.objects.all()[:500]
    serializer_class = apiCufSolSolicitud
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']

#74
class IfActaPermiso(viewsets.ModelViewSet):
    queryset = IfActa.objects.all()[:500]
    serializer_class = apiIfActa
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#75
class IfAnuAnulaotPermiso(viewsets.ModelViewSet):
    queryset = IfAnuAnulaot.objects.all()[:500]
    serializer_class = apiIfAnuAnulaot
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#79
class IfConsentimientoPermiso(viewsets.ModelViewSet):
    queryset = IfConsentimiento.objects.all()[:500]
    serializer_class = apiIfConsentimiento
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#81
class IfContactosGrillaPermiso(viewsets.ModelViewSet):
    queryset = IfContactosGrilla.objects.all()[:500]
    serializer_class = apiIfContactosGrilla
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#82
class IfCuerpoPermiso(viewsets.ModelViewSet):
    queryset = IfCuerpo.objects.all()[:500]
    serializer_class = apiIfCuerpo
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#83
class IfCuerpo2Permiso(viewsets.ModelViewSet):
    queryset = IfCuerpo2.objects.all()[:500]
    serializer_class = apiIfCuerpo2
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#84
class IfCuerpo3Permiso(viewsets.ModelViewSet):
    queryset = IfCuerpo3.objects.all()[:500]
    serializer_class = apiIfCuerpo3
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#85
class IfCuerpo4Permiso(viewsets.ModelViewSet):
    queryset = IfCuerpo4.objects.all()[:500]
    serializer_class = apiIfCuerpo4
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#86
class IfCuerpo5Permiso(viewsets.ModelViewSet):
    queryset = IfCuerpo5.objects.all()[:500]
    serializer_class = apiIfCuerpo5
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#87
class IfCuerpo6Permiso(viewsets.ModelViewSet):
    queryset = IfCuerpo6.objects.all()[:500]
    serializer_class = apiIfCuerpo6
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#88
class IfCuerpo7Permiso(viewsets.ModelViewSet):
    queryset = IfCuerpo7.objects.all()[:500]
    serializer_class = apiIfCuerpo7
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#89
class IfDesplazamientoPermiso(viewsets.ModelViewSet):
    queryset = IfDesplazamiento.objects.all()
    serializer_class = apiIfDesplazamiento
    filterset_fields = ['pen_idsolpadre']
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#92
class IfDocumentalGrillaPermiso(viewsets.ModelViewSet):
    queryset = IfDocumentalGrilla.objects.all()[:500]
    serializer_class = apiIfDocumentalGrilla
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#94
class IfEntornosPermiso(viewsets.ModelViewSet):
    queryset = IfEntornos.objects.all()[:500]
    serializer_class = apiIfEntornos
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
#99
class IfEntrevistaPermiso(viewsets.ModelViewSet):
    queryset = IfEntrevista.objects.all()
    serializer_class = apiIfEntrevista
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['en_ortr_001','pen_idsolicitud']
    http_method_names = ['get']
    
#100
class IfEntrevista2Permiso(viewsets.ModelViewSet):
    queryset = IfEntrevista2.objects.all()
    serializer_class = apiIfEntrevista2
    filterset_fields = ['pen_idsolicitud']
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get']
    
class IfGvpPermiso(viewsets.ModelViewSet):
    queryset = IfGvp.objects.all()
    serializer_class = apiIfgvp
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pen_idsolpadre']
    http_method_names = ['get']
    
class IfRepartoGralPte1Permiso(viewsets.ModelViewSet):
    queryset = IfRepartoGralPte1.objects.all()
    serializer_class = apiIfRepartoGralPte1
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['re_ortr_009']
    http_method_names = ['get']