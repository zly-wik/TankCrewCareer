from rest_framework.routers import SimpleRouter

from core.views import MissionObjectVS, MissionOptionsVS, VehicleVS

router = SimpleRouter()
router.register('missions', MissionOptionsVS, basename='missions')
router.register('mission-objs', MissionObjectVS, basename='mission-objs')
router.register('vehicles', VehicleVS, basename='vehicles')

urlpatterns = router.urls
