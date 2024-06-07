# config/management/commands/graphql_schema.py
from django.core.management.base import BaseCommand
from graphene import Schema
from graphql.utils.schema_printer import print_schema
from config.schema import schema


class Command(BaseCommand):
    help = 'Generate schema.graphql file'

    def handle(self, *args, **options):
        with open('schema.graphql', 'w') as f:
            schema_str = print_schema(schema.graphql_schema)
            f.write(schema_str)
            self.stdout.write(self.style.SUCCESS('Successfully generated schema.graphql'))
