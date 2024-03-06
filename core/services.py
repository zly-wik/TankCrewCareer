from core.enums import MissionObjectType

from core.enums import VehicleTypes



VEHICLE_SCRIPT_AND_MODEL = {
    VehicleTypes.PZ_IV.name: {
        'script': 'LuaScripts\\WorldObjects\\vehicles\\_pziv-g.txt',
        'model': 'graphics\\vehicles\\_pziv-g\\_pziv-g.mgm',
    },
    VehicleTypes.PZ_V_PANTHER.name: {
        'script': 'LuaScripts\\WorldObjects\\vehicles\\_pzv-d.txt',
        'model': 'graphics\\vehicles\\_pzv-d\\_pzv-d.mgm',
    },
    VehicleTypes.PZ_VI_TIGER.name: {
        'script': 'LuaScripts\\WorldObjects\\vehicles\\_pzvi-h1.txt',
        'model': 'graphics\\vehicles\\_pzvi-h1\\_pzvi-h1.mgm',
    },
    VehicleTypes.KV_1S.name: {
        'script': 'LuaScripts\\WorldObjects\\vehicles\\_kv1s.txt',
        'model': 'graphics\vehicles\\_kv1s\\_kv1s.mgm',
    },
    VehicleTypes.SU_152.name: {
        'script': 'LuaScripts\\WorldObjects\\vehicles\\_su152.txt',
        'model': 'graphics\\vehicles\\_su152\\_su152.mgm',
    },
}


def dict_to_dot_mission(object_type: MissionObjectType, data: dict) -> str:
    data_string: str = object_type
    data_string += '\n{\n'
    for key, value in data.items():
        if isinstance(value, list):
            data_string += f'{key} = {value};\n'
        elif isinstance(value, dict):
            data_string += dict_to_dot_mission(f'{key}', value)
        elif isinstance(value, int):
            data_string += f'{key} = {value};\n'
        elif key in {'Time', 'Date'}:
            data_string += f'{key} = {value};\n'
        elif key in {'WindLayers', 'Countries'}:
            data_string += key + '\n{\n' + value + '}\n' # v.strip()
        elif key == 'MissionObjects':
            data_string += '}\n\n' # We need to end Options block before
            for object in value:
                if object.object_type == MissionObjectType.Vehicle:
                    print(object.__dict__)
                data_string += object.dot_mission_format
                data_string += '}\n\n'
        else:
            data_string += f'{key} = "{value}";\n'
    # data_string += '}\n'

    print(data_string)
    return data_string


def get_vehicle_script_and_model(vehicle: VehicleTypes) -> tuple[str, str]:
    return VEHICLE_SCRIPT_AND_MODEL.get(vehicle)
