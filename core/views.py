from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from core.models import MissionObject, Mission, Vehicle
from core.serializers import MissionObjectSerializer, MissionSerializer, VehicleSerializer


class MissionObjectViewSet(ModelViewSet):
    queryset = MissionObject.objects.all()
    serializer_class = MissionObjectSerializer


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class MissionOptionsViewSet(ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    
    @action(detail=True, methods=['get'])
    def download(self, request, pk):
        mission = Mission.objects.get(pk=pk)
        mission.generate_mission(filename=mission.mission_name)
        
        return HttpResponseRedirect(self.reverse_action('detail', pk))
