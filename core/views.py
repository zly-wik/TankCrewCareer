from rest_framework.viewsets import ModelViewSet

from core.models import MissionObject, Mission
from core.serializers import MissionObjectSerializer, MissionSerializer


class MissionObjectVS(ModelViewSet):
    queryset = MissionObject.objects.all()
    serializer_class = MissionObjectSerializer

class MissionOptionsVS(ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer