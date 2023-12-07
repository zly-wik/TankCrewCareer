from rest_framework.serializers import ModelSerializer

from core.models import MissionObject


class MissionObjectSerializer(ModelSerializer):
    class Meta:
        model = MissionObject
        fields = ['pk', 'object_type', 'name', 'desc', 'mcu_targets', 'mcu_objects', 'position', 'properties']
