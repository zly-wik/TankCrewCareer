from rest_framework import serializers
from core.enums import MissionObjectType

from core.models import MissionObject, Mission, Vehicle


class MissionObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionObject
        fields = [
            'pk',
            'object_type',
            'name',
            'desc',
            'mcu_targets',
            'mcu_objects',
            'position',
            'properties',
            'attached_mission',
        ]


class VehicleSerializer(serializers.ModelSerializer):
    object_type = serializers.HiddenField(default=MissionObjectType.Vehicle)
    class Meta:
        model = Vehicle
        fields = [
            'pk',
            'object_type',
            'vehicle_type',
            'name',
            'desc',
            'position',
            'mcu_targets',
            'mcu_objects',
            'properties',
            'attached_mission',
            'link_tr_id',
            'script',
            'model',
            'country',
            'number_in_formation',
            'vulnerable',
            'engageable',
            'limit_ammo',
            'ai_level',
            'coop_start',
            'fuel',
        ]
        read_only_fields = [
            'pk',
            'link_tr_id',
            'object_type',
            'script',
            'model',
        ]


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        
        fields = [
            'pk',
            'mission_name',
            'lc_name',
            'lc_desc',
            'lc_author',
            'mission_time',
            'mission_date',
            'mission_properties',
            'wind_layers',
            'countries',
            'mission_objects',
        ]
        read_only_fields = [
            'pk',
        ]