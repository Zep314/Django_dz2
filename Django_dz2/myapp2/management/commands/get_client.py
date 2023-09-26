from django.core.management.base import BaseCommand
from ...models import Client
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Get client by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            logger.info(f'Successfully get client (id={pk}): {client}')
        else:
            logger.warning(f'Client (id={pk}) don\'t exist!')
        self.stdout.write(f'{client}')
