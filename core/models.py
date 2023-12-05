from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models
# Create your models here.
class BaseObject(models.Model):
    """Base object used as parent for each mission object."""
    # Model id field will be mission object Index field (in mission file).
    name = models.CharField(max_length=128)
    desc = models.CharField(max_length=512, null=True, blank=True)
    mcu_targets = models.ManyToManyField('BaseObject', blank=True, related_name='target_parent')
    mcu_objects = models.ManyToManyField('BaseObject', blank=True, related_name='object_parent')
    x_pos = models.IntegerField(default=0)
    y_pos = models.IntegerField(default=0)
    z_pos = models.IntegerField(default=0)
    x_ori = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(359)], help_text='mission-unit rotation 0-360*')
    y_ori = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(359)], help_text='mission-unit rotation 0-360*')
    z_ori = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(359)], help_text='mission-unit rotation 0-360*')

    def __str__(self) -> str:
        return f"[{self.pk}] {self.name}"
