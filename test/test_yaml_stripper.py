import os
import yaml
from tempfile import NamedTemporaryFile

from yaml_stripper import remove_fields


def test_remove_fields():
    input_yaml = {'name': 'John', 'age': 30, 'hobbies': ['reading', 'writing', 'swimming']}
    with NamedTemporaryFile(mode='w', delete=False) as f:
        yaml.dump(input_yaml, f)

    remove_fields(f.name, ['age'], f.name)

    with open(f.name, 'r') as f:
        output_yaml = yaml.load(f, Loader=yaml.FullLoader)
        assert 'age' not in output_yaml
        assert output_yaml['name'] == 'John'
        assert output_yaml['hobbies'] == ['reading', 'writing', 'swimming']

    os.remove(f.name)
