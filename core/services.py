from core.enums import MissionObjectType

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
                data_string += object.dot_mission_format
                data_string += '}\n\n'
        else:
            data_string += f'{key} = "{value}";\n'
    # data_string += '}\n'

    print(data_string)
    return data_string
