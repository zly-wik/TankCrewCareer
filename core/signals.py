from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from core.enums import MissionObjectType
from core.models import MissionObject, Vehicle
from core.services import get_vehicle_script_and_model

@receiver(post_save, sender=Vehicle)
def create_linked_translator_entity(sender, instance=None, created=False, **kwargs):
    if not instance:
        print('No vehicle instance error')
        return
    if created:
        properties = {
            'Enabled': 1,
            'MisObjID': instance.pk,
        }
        linked_tr = MissionObject.objects.create(
            name=instance.name + " linked translator",
            desc=instance.name + " linked translator entity",
            object_type=MissionObjectType.MCU_TR_Entity,
            position=instance.position,
            properties = properties,
            
            # attached_mission = instance.attached_mission,
        )
        linked_tr.save()

        # if instance.attached_mission:
            # instance.attached_mission.set(linked_tr)
                # linked_tr.attached_mission.set(instance)

        instance.link_tr_id = linked_tr
        instance.save()


@receiver(pre_save, sender=Vehicle)
def update_script_and_model_if_vehicle_type_changed(sender, instance=None, created=False, **kwargs):
    if not instance:
        return
    if instance.vehicle_type:
        vehicle_data = get_vehicle_script_and_model(instance.vehicle_type)
        instance.script = vehicle_data['script']
        instance.model = vehicle_data['model']


@receiver(pre_save, sender=Vehicle)
def copy_vehicle_fields_to_properties_field_from_mission_object(sender, instance=None, **kwargs):
    if not instance:
        return
    instance.properties = {
        **instance.properties,
        "LinkTrId": instance.link_tr_id.pk if instance.link_tr_id else 0, # If doesnt exist - dont add to properties
        "Script": instance.script.replace('\v', '\\v'),
        "Model": instance.model.replace('\v', '\\v'),
        "Country": instance.country,
        "NumberInFormation": instance.number_in_formation,
        "Vulnerable":  1 if instance.vulnerable else 0,
        "Engangeable": 1 if instance.engangeable else 0,
        "LimitAmmo": 1 if instance.limit_ammo else 0,
        "AILevel": instance.ai_level,
        "DamageReport": 50,
        "DamageThreshold": 1,
        "DeleteAfterDeath": 1,
        "CoopStart": 1 if instance.coop_start else 0,
        "Spotter": -1,
        "BeaconChannel": 0,
        "Callsign": 0,
        "PayloadId": 0,
        "WMMask": 1,
        "Fuel": instance.fuel,
        "Callnum": 0,
        "Skin": "",
        "RepairFriendlies": 0,
        "RehealFriendlies": 0,
        "RearmFriendlies": 0,
        "RefuelFriendlies": 0,
        "RepairTime": 0,
        "RehealTime": 0,
        "RearmTime": 0,
        "RefuelTime": 0,
        "MaintenanceRadius": 10,
        "TCode": "",
        "TCodeColor": ""
    }
    print(instance.properties)