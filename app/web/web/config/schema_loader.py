import os
from pathlib import Path


def load_schemas():
    schema_dir = Path(__file__).resolve().parent / 'graphql'
    schemas = []

    for root, _, files in os.walk(schema_dir):
        for file in files:
            if file.endswith('.graphql'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    schemas.append(f.read())

    return '\n'.join(schemas)
