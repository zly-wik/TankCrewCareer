from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

from typing import Optional

from core.enums import (
    MissionObjectType,
    VehicleTypes,
)
from core.services import dict_to_dot_mission

class MissionObject(models.Model):
    """Base object used for each mission object."""

    # Model Fields =  pk field will be mission object Index field (in mission file).
    object_type = models.CharField(max_length=100, choices=MissionObjectType.choices())
    name = models.CharField(max_length=128)
    desc = models.CharField(max_length=512, null=True, blank=True)
    mcu_targets = models.ManyToManyField('MissionObject', blank=True, related_name='target_parent')
    mcu_objects = models.ManyToManyField('MissionObject', blank=True, related_name='object_parent')
    position = models.JSONField(max_length=256)
    properties = models.JSONField(max_length=1024, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.object_type} | [{self.pk}] {self.name}'

    @property
    def index(self) -> int:
        return self.pk

    @property
    def mcu_targets_list(self) -> list:
        mcu_targets = []
        for mcu in self.mcu_targets.all():
            mcu_targets.append(mcu.index)
        return mcu_targets

    @property
    def mcu_objects_list(self) -> list:
        mcu_objects = []
        for mcu in self.mcu_objects.all():
            mcu_objects.append(mcu.index)
        return mcu_objects

    @property
    def dot_mission_format(self) -> str:
        object_keys = {
            'Index': self.pk,
            'Name': self.name,
            'Desc': self.desc,
            'Targets': self.mcu_targets_list,
            'Objects': self.mcu_objects_list,
            **self.position,
            **self.properties,
        }
        dot_mission_string = dict_to_dot_mission(self.object_type, object_keys)

        return dot_mission_string


class Vehicle(MissionObject):
    """Child class used for easier Vehicles management."""

    # Model Fields =  pk field will be mission object Index field (in mission file).
    link_tr_id = models.OneToOneField(MissionObject, related_name='mission_obj_id', on_delete=models.CASCADE, null=True, blank=True) # TODO Validate if MissionObjectType is MCU_TR_ENTITY and has MisObjID with self.pk
    vehicle_type = models.CharField(max_length=100, choices=VehicleTypes.choices())
    script = models.CharField(
        max_length=100,
        blank=True,
        null=False,
    )
    model = models.CharField(
        max_length=100,
        blank=True,
        null=False,
    )
    country = models.PositiveIntegerField()
    number_in_formation = models.PositiveIntegerField()
    vulnerable = models.BooleanField()
    engangeable = models.BooleanField()
    limit_ammo = models.BooleanField()
    ai_level = models.PositiveBigIntegerField()
    coop_start = models.BooleanField()
    fuel = models.PositiveIntegerField(validators=[
        MinValueValidator(0, 'Fuel can\'t be less than 0'),
        MaxValueValidator(100, 'Fuel can\'t be more than 100 %')
    ])
    
    @property
    def dot_mission_format(self) -> str:
        object_keys = {
            'Index': self.pk,
            'Name': self.name,
            'Desc': self.desc,
            'Targets': self.mcu_targets_list,
            'Objects': self.mcu_objects_list,
            'position': self.position,
            'LinkTrId': self.link_tr_id,
            'Script': self.script,
            'Model': self.model,
            'Country': self.country,
            'NumberInFormation': self.number_in_formation,
            'Vulnerable': self.vulnerable,
            'Engangeable': self.engangeable,
            'LimitAmmo': self.limit_ammo,
            'AILevel': self.ai_level,
            'CoopStart': self.coop_start,
            'Fuel': self.fuel,
            **self.position,
            **self.properties,
        }
        dot_mission_string = dict_to_dot_mission(self.object_type, object_keys)

        return dot_mission_string


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
    
    dot_mission_string: str = None
    
    def generate_mission(self, filename: Optional[str]) -> str|None:
        object_keys = {
            'LCName': self.lc_name,
            'LCDesc': self.lc_desc,
            'LCAuthor': self.lc_author,
            'Time': self.formatted_time,
            'Date': self.formatted_date,
            **self.other_required_fields,
            'WindLayers': self.formatted_wind_layers,
            'Countries': self.formatted_countries,
            'MissionObjects': self.mission_objects.all(),
        }
        self.dot_mission_string = '# Mission File Version = 1.0;\n\n'
        self.dot_mission_string += dict_to_dot_mission(MissionObjectType.OPTIONS, object_keys)
        self.dot_mission_string += '\n\n# end of file'
        
        if not filename:
            return self.dot_mission_string
        
        with open(f'{filename}.Mission', 'w') as file:
            file.write(self.dot_mission_string)
        
        return file

    
    @property
    def formatted_time(self) -> str:
        string_time = str(self.mission_time)
        time: str = string_time[0:2] + ':'
        time += string_time[2:4] + ':'
        time += string_time[4:6]
        return time
    
    @property
    def formatted_date(self) -> str:
        string_date = str(self.mission_date)
        date: str = string_date[0:2] + '.'
        date += string_date[2:4] + '.'
        date += string_date[4:8]
        return date

    @property
    def formatted_wind_layers(self) -> str:
        # NOTE: As it's not important field at all, for now we just return valid WindLayers string with default (0) values.
        return (
            "0 :     0 :     0;\n"
            "500 :     0 :     0;\n"
            "1000 :     0 :     0;\n"
            "2000 :     0 :     0;\n"
            "5000 :     0 :     0;\n"
        )

    @property
    def formatted_countries(self) -> str:
        # NOTE: As it's not important field at all, for now we just return valid Countries string with default values.
        return (
          "0 : 0;\n"
          "101 : 1;\n"
          "102 : 1;\n"
          "103 : 1;\n"
          "201 : 2;\n"
          "202 : 2;\n"
          "203 : 2;\n"
          "301 : 3;\n"
          "302 : 3;\n"
          "303 : 3;\n"
          "304 : 3;\n"
          "305 : 3;\n"
          "401 : 4;\n"
          "402 : 4;\n"
        )

    @property
    def other_required_fields(self) -> dict:
        return {
            'HMap': r"graphics\landscape\height.hini",
            'Textures': r"graphics\landscape\textures.tini",
            'Forests': r"graphics\landscape\trees\woods.wds",
            'Layers': "",
            'GuiMap': "lapino-winter",
            'SeasonPrefix': "wi",
            'MissionType': 0,
            'AqmId': 0,
            'CloudLevel': 500,
            'CloudHeight': 500,
            'PrecLevel': 0,
            'PrecType': 0,
            'CloudConfig': r"winter\00_clear_00\sky.ini",
            'SeaState': 0,
            'Turbulence': 0,
            'TempPressLevel': 0,
            'Temperature': -15,
            'Pressure': 760,
            'Haze': 0,
            'LayerFog': 0,
        }