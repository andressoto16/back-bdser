from django.urls import path, include
from rest_framework import routers
from conexionbd.api import *


app_name = 'conexionbd'

router = routers.DefaultRouter()
router.register('areeval', AReevalPermiso, basename='areeval')
router.register('usuario', AccUsuUsuarioPermiso, basename='usuario')
router.register('genera', CerActgGeneraPermiso, basename='genera')
router.register('agenda', CerAgeAgendaPermiso, basename='agenda')
router.register('cambiocalidad', CerCalCambioCalidadPermiso, basename='cambiocalidad')
router.register('cerrem', CerCerCerremPermiso, basename='cerrem')
router.register('medida', CerDetMedidaPermiso, basename='medida')
router.register('valoresindicecol', CerDetValoresIndColPermiso, basename='valoresindicecol')
router.register('evaluados', CerEvaEvaluadoPermiso, basename='evaluados')
router.register('comite', CerSegComitePermiso, basename='comite')
router.register('comite2', CerSeg2ComitePermiso, basename='comite2')
router.register('carcargues', CufCarCarguesPermiso, basename='carcargues')
router.register('rutaformatos', CufForFormatosPermiso, basename='rutaformatos')
router.register('solicitud', CufSolSolicitudPermiso, basename='solicitud')
router.register('actas', IfActaPermiso, basename='actas')
router.register('anulaot', IfAnuAnulaotPermiso, basename='anulaot')
router.register('consentimiento', IfConsentimientoPermiso, basename='consentimiento')
router.register('contacto', IfContactosGrillaPermiso, basename='contacto')
router.register('cuerpo1', IfCuerpoPermiso, basename='cuerpo1')
router.register('cuerpo2', IfCuerpo2Permiso, basename='cuerpo2')
router.register('cuerpo3', IfCuerpo3Permiso, basename='cuerpo3')
router.register('cuerpo4', IfCuerpo4Permiso, basename='cuerpo4')
router.register('cuerpo5', IfCuerpo5Permiso, basename='cuerpo5')
router.register('cuerpo6', IfCuerpo6Permiso, basename='cuerpo6')
router.register('cuerpo7', IfCuerpo7Permiso, basename='cuerpo7')
router.register('desplazamiento', IfDesplazamientoPermiso, basename='desplazamiento')
router.register('documentalgrilla', IfDocumentalGrillaPermiso, basename='documentalgrilla')
router.register('entorno', IfEntornosPermiso, basename='entorno')
router.register('entrevista', IfEntrevistaPermiso, basename='entrevista')
router.register('entrevista2', IfEntrevista2Permiso, basename='entrevista2')
router.register('gvp', IfGvpPermiso, basename='gvp')
router.register('reparto1', IfRepartoGralPte1Permiso, basename='reparto1')










urlpatterns = [
    path('', include(router.urls)),
]