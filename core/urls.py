from rest_framework.routers import SimpleRouter

from core.views import MissionObjectVS, MissionOptionsVS

router = SimpleRouter()
router.register('mission', MissionOptionsVS)
router.register('mission-obj', MissionObjectVS)

urlpatterns = router.urls
