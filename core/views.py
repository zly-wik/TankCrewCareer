from rest_framework.viewsets import ModelViewSet

from core.models import BaseObject
from core.serializers import BaseObjectSerializer


class BaseObjectVS(ModelViewSet):
    queryset = BaseObject.objects.all()
    serializer_class = BaseObjectSerializer
