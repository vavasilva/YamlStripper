import argparse
from .yaml_stripper import remove_fields


def main():
    parser = argparse.ArgumentParser(description='YAML Stripper')
    parser.add_argument('input_file', help='Input YAML file path')
    parser.add_argument('output_file', help='Output YAML file path')
    parser.add_argument('-f', '--fields', nargs='+', help='Fields to remove from the YAML file')
    args = parser.parse_args()
    remove_fields(args.input_file, args.fields, args.output_file)
