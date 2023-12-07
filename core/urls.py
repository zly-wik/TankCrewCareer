from rest_framework.routers import SimpleRouter

from core.views import MissionObjectVS

router = SimpleRouter()
router.register('mission-obj', MissionObjectVS)

urlpatterns = router.urls
