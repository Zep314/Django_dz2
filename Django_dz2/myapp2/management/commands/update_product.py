from django.core.management.base import BaseCommand
from ...models import Product
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Пример работы с таблицей товаров: Изменение данных об одном конкретном товаре из базы данных
    """
    help = "Update product name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('name', type=str, help='Product name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        product = Product.objects.filter(pk=pk).first()
        product.name = name
        product.save()
        self.stdout.write(f'{product}')
        if product is not None:
            logger.info(f'Successfully update client (id={pk}): {product}')
        else:
            logger.warning(f'Product (id={pk}) don\'t exist!')
        self.stdout.write(f'{product}')
