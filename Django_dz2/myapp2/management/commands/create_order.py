from django.core.management.base import BaseCommand
from ...models import Order, Client, Product
import decimal
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        client_pk = 1
        client = Client.objects.filter(pk=client_pk).first()

        products = Product.objects.filter(name__contains="Tesla")

        order = Order(id_client=client,
                      total_price=decimal.Decimal('321.09'))
        order.save()

        order.products.add(products)


        logger.info(f'Successfully create order: {order}')
        self.stdout.write(f'{order}')
