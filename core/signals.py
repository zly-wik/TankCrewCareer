from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from core.enums import MissionObjectType
from core.models import MissionObject, Vehicle
from core.services import get_vehicle_script_and_model

@receiver(post_save, sender=Vehicle)
def create_linked_translator_entity(sender, instance=None, created=False, **kwargs):
    if not instance:
        return
    if created:
        linked_tr = MissionObject.objects.create(
            name=instance.name + " linked translator",
            desc=instance.name + " linked translator entity",
            object_type=MissionObjectType.MCU_TR_ENTITY,
            position=instance.position
        )
        linked_tr.save()
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
