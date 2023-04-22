# YamlStripper

YamlStripper is a Python command-line tool for removing specified fields from YAML files.

## Installation

To use YamlStripper, you need to have Python 3 installed on your computer. You can download and install Python 3 from the official Python website: https://www.python.org/downloads/

After installing Python 3, you can install YamlStripper using pip, the Python package manager:

```
pip install yaml-stripper
```

## Usage

To use YamlStripper, open a command prompt or terminal window and type the following command:

```
yaml-stripper input_file output_file -f field1 field2 ...
```

where:

- `input_file` - The input YAML file to remove fields from.
- `output_file` - The output YAML file without the specified fields.
- `-f field1 field2 ...` - The fields to remove from the input YAML file.

For example, if you have a YAML file called `example.yaml` with the following contents:

```yaml
name: John
age: 30
email: john@example.com
phone: 123-456-7890
```

and you want to remove the `email` and `phone` fields from this YAML file and save the result in a new file called `stripped.yaml`, you can use the following command:

```
yaml-stripper example.yaml stripped.yaml -f email phone
```

After running the command, a new file called `stripped.yaml` will be created with the following contents:

```yaml
name: John
age: 30
```

## Examples

Here are some more examples of how to use YamlStripper:

### Example 1

Suppose you have a YAML file called `data.yaml` with the following contents:

```yaml
name: Alice
age: 25
email: alice@example.com
phone: 987-654-3210
address:
  street: 123 Main St
  city: Anytown
  state: CA
  zip: 12345
```

You want to remove the `email` and `phone` fields from this YAML file and save the result in a new file called `stripped.yaml`. Here's how you can use YamlStripper to achieve this:

```
yaml-stripper data.yaml stripped.yaml -f email phone
```

After running the command, a new file called `stripped.yaml` will be created with the following contents:

```yaml
name: Alice
age: 25
address:
  street: 123 Main St
  city: Anytown
  state: CA
  zip: 12345
```

### Example 2

Suppose you have a YAML file called `config.yaml` with the following contents:

```yaml
debug: true
port: 8000
database:
  host: localhost
  port: 5432
  name: mydb
  user: myuser
  password: mypass
```

You want to remove the `debug` field from this YAML file and save the result in a new file called `stripped.yaml`. Here's how you can use YamlStripper to achieve this:

```
yaml-stripper config.yaml stripped.yaml -f debug
```

After running the command, a new file called `stripped.yaml` will be created with the following contents:

```yaml
port: 8000
database:
  host: localhost
  port: 5432
  name: mydb
  user: myuser
 