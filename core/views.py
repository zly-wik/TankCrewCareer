from rest_framework.viewsets import ModelViewSet

from core.models import MissionObject
from core.serializers import MissionObjectSerializer


class MissionObjectVS(ModelViewSet):
    queryset = MissionObject.objects.all()
    serializer_class = MissionObjectSerializer
