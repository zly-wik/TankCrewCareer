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


class Mission(models.Model):
    """Mission options used in '.Mission Options' object."""

    mission_name = models.CharField(max_length=256, help_text='mission name is not used in .Mission file itself, but it helps searcing missions')
    lc_name = models.PositiveIntegerField()
    lc_desc = models.PositiveIntegerField()
    lc_author = models.PositiveIntegerField()
    mission_time = models.PositiveIntegerField()  # 123000 = 12:30:00 ect.
    mission_date = models.PositiveIntegerField()  # 19111942 - 19.11.1924
    mission_properties = models.JSONField(max_length=1024)
    wind_layers = models.JSONField(max_length=256)
    countries = models.JSONField(max_length=256)
    mission_objects = models.ManyToManyField(MissionObject, blank=True, related_name='attached_mission')