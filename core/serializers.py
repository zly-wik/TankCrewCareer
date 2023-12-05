from rest_framework.serializers import ModelSerializer

from core.models import BaseObject


class BaseObjectSerializer(ModelSerializer):
    class Meta:
        model = BaseObject
        fields = ['id', 'name', 'desc', 'mcu_targets', 'mcu_objects', 'x_pos', 'y_pos', 'z_pos', 'x_ori', 'y_ori', 'z_ori']
