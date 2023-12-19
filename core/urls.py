from rest_framework.routers import SimpleRouter

from core.views import MissionObjectVS, MissionOptionsVS

router = SimpleRouter()
router.register('mission', MissionOptionsVS, basename='mission')
router.register('mission-obj', MissionObjectVS, basename='mission-obj')

urlpatterns = router.urls
