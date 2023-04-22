import os
import pytest
import yaml
from tempfile import NamedTemporaryFile

from YamlStripper.yaml_stripper import remove_fields


@pytest.fixture
def input_yaml():
    return {'name': 'John', 'age': 30, 'hobbies': ['reading', 'writing', 'swimming']}


def test_remove_fields(input_yaml):
    with NamedTemporaryFile(mode='w', delete=False) as f:
        yaml.dump(input_yaml, f)

    remove_fields(f.name, ['age'], f.name)

    with open(f.name, 'r') as f:
        output_yaml = yaml.load(f, Loader=yaml.FullLoader)
        assert 'age' not in output_yaml
        assert output_yaml['name'] == 'John'
        assert output_yaml['hobbies'] == ['reading', 'writing', 'swimming']

    os.remove(f.name)


def test_should_not_create_a_file(input_yaml):
    with NamedTemporaryFile(mode='w', delete=False) as f:
        yaml.dump(input_yaml, f)

    remove_fields(f.name, ['field_that_not_exists'], 'this_file_will_not_exist.yml')

    with pytest.raises(FileNotFoundError) as exception:
        with open('this_file_will_not_exist.yml', 'r') as f:
            yaml.load(f, Loader=yaml.FullLoader)
    assert str(exception.value) == "[Errno 2] No such file or directory: 'this_file_will_not_exist.yml'"

    os.remove(f.name)
