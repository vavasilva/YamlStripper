import argparse
import yaml
import copy


def remove_field(data, field):
    """
    Recursively remove field from data
    """
    if field in data:
        del data[field]
    for k, v in data.items():
        if isinstance(v, dict):
            remove_field(v, field)
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    remove_field(item, field)


def remove_fields(yaml_file, fields_to_remove, new_yaml_file):
    """Remove specified fields from a YAML file.

    Args:
        yaml_file (str): The input YAML file.
        fields_to_remove (list): The fields to remove.
        new_yaml_file (str): The output YAML file without the specified fields.

    """
    with open(yaml_file, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    old_yaml_data = copy.deepcopy(data)
    for field in fields_to_remove:
        remove_field(data, field)

    if old_yaml_data == data:
        return

    # Remove empty dictionary items
    data = {k:v for k, v in data.items() if v}

    with open(new_yaml_file, 'w') as f:
        yaml.dump(data, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Remove specified fields from a YAML file')

    parser.add_argument('yaml_file', type=str, help='The input YAML file')
    parser.add_argument('new_yaml_file', type=str,
                        help='The output YAML file without the specified fields')
    parser.add_argument('-f', '--fields', type=str, nargs='+',
                        help='The fields to remove', required=True)

    args = parser.parse_args()

    remove_fields(args.yaml_file, args.fields, args.new_yaml_file)
