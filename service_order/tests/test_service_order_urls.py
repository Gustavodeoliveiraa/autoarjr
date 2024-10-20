from django.test import TestCase
from django.urls import reverse
from service_order.models import ServiceOrder


class TestServiceOrderUlr(TestCase):
    def setUp(self) -> None:
        ServiceOrder.objects.create(
            client_name='pedro', client_cellphone='11939230072',
            car_model='fusca', car_plate='ASX-1010', service_price=200,
            service='Troca do compressor', paid=False
        )
        return super().setUp()

    def test_if_url_of_list_service_order_return_200(self):
        response = self.client.get(reverse('service_order:list'))

        self.assertEqual(response.status_code, 200)

    def test_if_url_of_create_service_order_return_200(self):
        response = self.client.get(reverse('service_order:register'))

        self.assertEqual(response.status_code, 200)

    def test_if_url_of_update_service_order_return_200(self):
        response = self.client.get(reverse('service_order:update', args=(1,)))

        self.assertEqual(response.status_code, 200)

    def test_if_url_of_delete_service_order_return_200(self):
        response = self.client.get(reverse('service_order:delete', args=(1,)))

        self.assertEqual(response.status_code, 200)
