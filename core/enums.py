from enum import StrEnum

class MissionObjectType(StrEnum):
    OPTIONS = 'Options'
    MCU_TR_AI_Poi = 'MCU_TR_AI_Poi'
    MCU_TR_MissionBegin = 'MCU_TR_MissionBegin'
    MCU_TR_MissionEnd = 'MCU_TR_MissionEnd'
    MCU_TR_MissionObjective = 'MCU_TR_MissionObjective'
    MCU_TR_Subtitle = 'MCU_TR_Subtitle'
    MCU_Activate = 'MCU_Activate'
    MCU_Deactivate = 'MCU_Deactivate'
    MCU_Timer = 'MCU_Timer'
    MCU_Waypoint = 'MCU_Waypoint'
    MCU_CMD_AttackTarget = 'MCU_CMD_AttackTarget'
    MCU_CMD_AttackArea = 'MCU_CMD_AttackArea'
    MCU_CMD_Cover = 'MCU_CMD_Cover'
    MCU_CMD_Move = 'MCU_CMD_Move'
    
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)