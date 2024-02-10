import csv
from django.core.management.base import BaseCommand
from actors.models import Actor
from datetime import datetime


class Command(BaseCommand):
    help = 'Comando para importar lista de atores.'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='Nome do arquivo CSV na raiz do projeto.')

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(name))

                Actor.objects.create(name=name, birthday=birthday, nationality=nationality)

            self.stdout.write(self.style.SUCCESS('ATORES IMPORTADOS COM SUCESSO!'))
