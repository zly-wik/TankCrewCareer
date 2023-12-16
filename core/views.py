from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from core.models import MissionObject, Mission
from core.serializers import MissionObjectSerializer, MissionSerializer


class MissionObjectVS(ModelViewSet):
    queryset = MissionObject.objects.all()
    serializer_class = MissionObjectSerializer

    # NOTE: DO NOT delete. Commented code is used while debugging
    # def retrieve(self, request, pk): 
    #     data_string = MissionObject.objects.get(pk=pk).dot_mission_format
        
    #     return HttpResponse(data_string)

class MissionOptionsVS(ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    
    def retrieve(self, request, pk):
        
        Mission.objects.get(pk=pk).generate_mission('testMission')
        return HttpResponse('Ok.')