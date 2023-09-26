from django.core.management.base import BaseCommand
from ...models import Client
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com',
                        phone='+7-123-456-78-90', address='221B Baker Street, London NW1 6XE, England')
        client.save()
        logger.info(f'Successfully create client: {client}')
        self.stdout.write(f'{client}')
