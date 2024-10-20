# type: ignore
from django.test import TestCase
from django.urls import reverse
from service_order.models import ServiceOrder
from utils.create_service_order_function import (
    shortcut_create_service_order as create_order
)


class TestServiceOrderView(TestCase):
    def setUp(self) -> None:
        create_order(
            'teste01', '(00) 00000-0000', 'car_01', 'ZZZ-1111', 500,
            'Troca do compressor, Troca do condensador', False
        )
        return super().setUp()

    # Create
    def test_if_service_order_create_view_function_with_successful(self):
        data = {
            'client_name': "alfredo", 'client_cellphone': '(11) 99999-9999',
            'car_model': 'corsa', 'car_plate': 'AAA-9999', 'service_price': 200,
            'service': 'Troca do compressor, Troca do condensador',
            'paid': False
        }

        response = self.client.post(reverse('service_order:register'), data)
        response_data = self.client.get(reverse('service_order:list'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response_data.status_code, 200)
        self.assertInHTML('Alfredo', response_data.content.decode())
        self.assertInHTML('(11) 99999-9999', response_data.content.decode())
        self.assertInHTML('corsa', response_data.content.decode())
        self.assertInHTML('AAA-9999', response_data.content.decode())
        self.assertInHTML('200,00', response_data.content.decode())

    # Read
    def test_if_service_order_list_view_function_with_successful(self):
        response = self.client.get(reverse('service_order:list'))

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Teste01', response.content.decode())
        self.assertInHTML('(00) 00000-0000', response.content.decode())
        self.assertInHTML('car_01', response.content.decode())
        self.assertInHTML('ZZZ-1111', response.content.decode())
        self.assertInHTML('500,00', response.content.decode())

    # Read with Filter (client_name)
    def test_if_service_order_will_be_filtered_by_client_name_with_successful(self):
        create_order()
        create_order(client_name='teste01')

        response = self.client.get(
            reverse('service_order:list') + '?client_name='
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Teste01', response.content.decode())
        self.assertInHTML('Teste__', response.content.decode())

        response = self.client.get(
            reverse('service_order:list') + '?client_name=teste01'
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Teste01', response.content.decode())
        self.assertNotIn('Teste__', response.content.decode())

    # Read with Filter (client_cellphone)
    def test_if_service_order_will_be_filtered_by_client_cellphone_with_successful(self):
        create_order()
        create_order(client_cellphone='(00) 00000-0000')

        response = self.client.get(
            reverse('service_order:list') + '?client_cellphone='
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('(00) 00000-0000', response.content.decode())
        self.assertInHTML('(11) 99999-9999', response.content.decode())

        response_filtered = self.client.get(
            reverse('service_order:list') + '?client_cellphone=(00) 00000-0000'
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('(00) 00000-0000', response_filtered.content.decode())
        self.assertNotIn('(11) 99999-9999', response_filtered.content.decode())

    # Read with Filter (car_model)
    def test_if_service_order_will_be_filtered_by_car_model_with_successful(self):
        create_order()
        create_order(car_model='fusca')

        response = self.client.get(
            reverse('service_order:list') + '?car_model='
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('fusca', response.content.decode())
        self.assertInHTML('opala', response.content.decode())

        response_filtered = self.client.get(
            reverse('service_order:list') + '?car_model=opala'
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('opala', response_filtered.content.decode())
        self.assertNotIn('fusca', response_filtered.content.decode())

    # Read with Filter (car_plate)
    def test_if_service_order_will_be_filtered_by_car_plate_with_successful(self):
        create_order()
        create_order(car_plate='EEE-4004')

        response = self.client.get(
            reverse('service_order:list') + '?car_plate='
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('EEE-4004', response.content.decode())
        self.assertInHTML('AAA-0000', response.content.decode())

        response_filtered = self.client.get(
            reverse('service_order:list') + '?car_plate=AAA-0000'
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('AAA-0000', response_filtered.content.decode())
        self.assertNotIn('EEE-4004', response_filtered.content.decode())

    # Read with Filter (paid)
    def test_if_service_order_will_be_filtered_by_paid_with_successful(self):
        create_order(client_name='client_p', paid=True)

        response = self.client.get(
            reverse('service_order:list') + '?paid='
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Client_P', response.content.decode())
        self.assertInHTML('Teste01', response.content.decode())

        response_filtered = self.client.get(
            reverse('service_order:list') + '?paid=1'
        )
        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Client_P', response_filtered.content.decode())
        self.assertNotIn('Teste01', response_filtered.content.decode())

    # Update
    def test_if_service_order_will_be_updated_with_successful(self):

        data = {
            'client_name': "name_att", 'client_cellphone': '(22) 22222-2222',
            'car_model': 'car_att', 'car_plate': 'AAA-9999', 'service_price': 200,
            'service': 'service_att',
            'paid': False
        }
        response = self.client.post(
            reverse('service_order:update', args=(1,)), data
        )

        self.assertEqual(response.status_code, 302)
        service_order = ServiceOrder.objects.all().first()

        self.assertEqual(data['client_name'], service_order.client_name)
        self.assertEqual(data['client_cellphone'], service_order.client_cellphone)
        self.assertEqual(data['car_model'], service_order.car_model)
        self.assertEqual(data['car_plate'], service_order.car_plate)
        self.assertEqual(data['service'], service_order.service)

        self.assertNotEqual(service_order.client_name, 'teste01')

    # Delete
    def test_if_service_order_will_be_deleted_with_successful(self):

        service_order = ServiceOrder.objects.all().first()
        self.assertIsNotNone(service_order)

        response = self.client.post(
            reverse('service_order:delete', args=(1,))
        )

        service_order_deleted = ServiceOrder.objects.all().first()
        self.assertEqual(response.status_code, 302)
        self.assertIsNone(service_order_deleted)
