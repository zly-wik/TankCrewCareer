from rest_framework.routers import SimpleRouter

from core.views import MissionObjectVS, MissionOptionsVS, VehicleVS

router = SimpleRouter()
router.register('mission', MissionOptionsVS, basename='mission')
router.register('mission-obj', MissionObjectVS, basename='mission-obj')
router.register('vehicle', VehicleVS, basename='vehicle')

urlpatterns = router.urls
