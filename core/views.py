from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from core.models import MissionObject, Mission, Vehicle
from core.serializers import MissionObjectSerializer, MissionSerializer, VehicleSerializer


class MissionObjectVS(ModelViewSet):
    queryset = MissionObject.objects.all()
    serializer_class = MissionObjectSerializer

    # NOTE: DO NOT delete. Commented code is used while debugging
    # def retrieve(self, request, pk): 
    #     data_string = MissionObject.objects.get(pk=pk).dot_mission_format
        
    #     return HttpResponse(data_string)


class VehicleVS(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class MissionOptionsVS(ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    
    # NOTE: DO NOT delete. Commented code is used while debugging
    @action(detail=True, methods=['get'])
    def download(self, request, pk):
        mission = Mission.objects.get(pk=pk)
        mission.generate_mission(filename=mission.mission_name)
        
        return HttpResponseRedirect(self.reverse_action('detail', pk))
