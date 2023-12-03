from rest_framework.serializers import ModelSerializer

from core.models import BaseObject


class BaseObjectSerializer(ModelSerializer):
    class Meta:
        model = BaseObject
        fields = ['index', 'name', 'desc']