from django.db.models.signals import post_save
from django.dispatch import receiver

from core.enums import MissionObjectType
from core.models import MissionObject, Vehicle


@receiver(post_save, sender=Vehicle)
def create_linked_translator_entity(sender, instance=None, created=False, **kwargs):
    print("Signal triggered")
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
        print("Linked translator entity created")