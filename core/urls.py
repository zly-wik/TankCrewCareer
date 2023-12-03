from django.urls import path
from rest_framework.routers import SimpleRouter

from core.views import BaseObjectVS

router = SimpleRouter()
router.register('base-obj', BaseObjectVS)

urlpatterns = router.urls
