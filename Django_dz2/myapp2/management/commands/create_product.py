from django.core.management.base import BaseCommand
from ...models import Product
import decimal
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Пример работы с таблицей товаров: Создание товара
    """
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='Tesla', description='Best electric car'
                          ,price=decimal.Decimal('123456.78'), amount=11)
        product.save()
        logger.info(f'Successfully create product: {product}')
        self.stdout.write(f'{product}')
