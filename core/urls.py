from rest_framework.routers import SimpleRouter

from core.views import MissionObjectViewSet, MissionOptionsViewSet, VehicleViewSet

router = SimpleRouter()
router.register('missions', MissionOptionsViewSet, basename='missions')
router.register('mission-objs', MissionObjectViewSet, basename='mission-objs')
router.register('vehicles', VehicleViewSet, basename='vehicles')

urlpatterns = router.urls
