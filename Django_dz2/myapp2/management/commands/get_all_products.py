from django.core.management.base import BaseCommand
from ...models import Product
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Get all products."

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        logger.info('Get all products!')
        self.stdout.write(f'{products}')
