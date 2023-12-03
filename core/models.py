from django.db import models

# Create your models here.
class BaseObject(models.Model):
    index = models.PositiveIntegerField(unique=True, db_index=True)
    name = models.CharField(max_length=128)
    desc = models.CharField(max_length=512)
    mcu_targets = models.ForeignKey('BaseObject', on_delete=models.SET_NULL, to_field='index', null=True, blank=True, related_name='target_parent')
    mcu_objects = models.ForeignKey('BaseObject', on_delete=models.SET_NULL, to_field='index', null=True, blank=True, related_name='object_parent')
    x_pos = models.IntegerField(help_text='divided by 1000 will be mission-unit position')
    y_pos = models.IntegerField(help_text='divided by 1000 will be mission-unit position')
    z_pos = models.IntegerField(help_text='divided by 1000 will be mission-unit position')
    x_ori = models.SmallIntegerField(help_text='mission-unit rotation 0-360*')
    y_ori = models.SmallIntegerField(help_text='mission-unit rotation 0-360*')
    z_ori = models.SmallIntegerField(help_text='mission-unit rotation 0-360*')

    def __str__(self) -> str:
        return f"[{self.index}] {self.name}"