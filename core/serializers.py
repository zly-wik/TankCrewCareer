from rest_framework.serializers import ModelSerializer

from core.models import MissionObject, Mission


class MissionObjectSerializer(ModelSerializer):
    class Meta:
        model = MissionObject
        fields = ['pk', 'object_type', 'name', 'desc', 'mcu_targets', 'mcu_objects', 'position', 'properties', 'attached_mission']


class MissionSerializer(ModelSerializer):
    class Meta:
        model = Mission
        fields = ['pk', 'mission_name', 'lc_name', 'lc_desc', 'lc_author', 'mission_time', 'mission_date', 'mission_properties', 'wind_layers', 'countries', 'mission_objects']
        read_only_fields = ['pk', 'lc_name', 'lc_desc', 'lc_author']