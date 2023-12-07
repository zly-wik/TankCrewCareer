from django.db import models

from core.enums import MissionObjectType


class MissionObject(models.Model):
    """Base object used as parent for each mission object."""

    # Model Fields =  pk field will be mission object Index field (in mission file).
    object_type = models.CharField(max_length=100, choices=MissionObjectType.choices())
    name = models.CharField(max_length=128)
    desc = models.CharField(max_length=512, null=True, blank=True)
    mcu_targets = models.ManyToManyField('MissionObject', blank=True, related_name='target_parent')
    mcu_objects = models.ManyToManyField('MissionObject', blank=True, related_name='object_parent')
    position = models.JSONField(max_length=256)
    properties = models.JSONField(max_length=1024)

    def __str__(self) -> str:
        return f'{self.object_type} | [{self.pk}] {self.name}'