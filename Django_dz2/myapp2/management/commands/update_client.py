from django.core.management.base import BaseCommand
from ...models import Client
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Update client name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        client = Client.objects.filter(pk=pk).first()
        client.name = name
        client.save()
        self.stdout.write(f'{client}')
        if client is not None:
            logger.info(f'Successfully update client (id={pk}): {client}')
        else:
            logger.warning(f'Client (id={pk}) don\'t exist!')
        self.stdout.write(f'{client}')
