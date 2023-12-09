# Generated by Django 4.2.7 on 2023-12-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MissionObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_type', models.CharField(choices=[('MCU_TR_AI_Poi', 'MCU_TR_AI_Poi'), ('MCU_TR_MissionBegin', 'MCU_TR_MissionBegin'), ('MCU_TR_MissionEnd', 'MCU_TR_MissionEnd'), ('MCU_TR_MissionObjective', 'MCU_TR_MissionObjective'), ('MCU_TR_Subtitle', 'MCU_TR_Subtitle'), ('MCU_Activate', 'MCU_Activate'), ('MCU_Deactivate', 'MCU_Deactivate'), ('MCU_Timer', 'MCU_Timer'), ('MCU_Waypoint', 'MCU_Waypoint'), ('MCU_CMD_AttackTarget', 'MCU_CMD_AttackTarget'), ('MCU_CMD_AttackArea', 'MCU_CMD_AttackArea'), ('MCU_CMD_Cover', 'MCU_CMD_Cover'), ('MCU_CMD_Move', 'MCU_CMD_Move')], max_length=100)),
                ('name', models.CharField(max_length=128)),
                ('desc', models.CharField(blank=True, max_length=512, null=True)),
                ('position', models.JSONField(max_length=256)),
                ('properties', models.JSONField(max_length=1024)),
                ('mcu_objects', models.ManyToManyField(blank=True, related_name='object_parent', to='core.missionobject')),
                ('mcu_targets', models.ManyToManyField(blank=True, related_name='target_parent', to='core.missionobject')),
            ],
        ),
    ]
