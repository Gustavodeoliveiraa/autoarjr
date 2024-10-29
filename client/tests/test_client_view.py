# type: ignore

from django.test import TestCase
from django.test import Client as TestClient
from django.urls import reverse
from client.models import Client
from datetime import date, timedelta
from django.contrib.auth.models import User


class TestClientView(TestCase):
    def setUp(self) -> None:

        self.user = User.objects.create_superuser(username='gustavo', password='12345')
        self.client = TestClient()
        self.client.login(username='gustavo', password='12345')

        Client.objects.create(
            client_name='gustavo',
            cellphone="11030239923",
            car_model="sandero",
            car_plate="asx-1030"
        )
        Client.objects.create(
            client_name='jose',
            cellphone="11111111111",
            car_model="corsa",
            car_plate="zzz-0000"
        )
        return super().setUp()

    # read
    def test_if_list_view_client_function_with_success(self):

        response = self.client.get(reverse('client:list'))

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Gustavo', response.content.decode())

    # Read with filter
    def test_if_client_is_filtered_by_name_with_successful(self):
        response = self.client.get(
            reverse('client:list') + '?name=gustavo'
        )

        print(reverse('client:list') + '?name=gustavo')

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Gustavo', response.content.decode())
        self.assertNotIn('jose', response.content.decode())

    # Read with filter
    def test_if_client_is_filtered_by_cellphone_with_successful(self):
        response = self.client.get(
            reverse('client:list') + '?cellphone=11030239923'
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Gustavo', response.content.decode())
        self.assertInHTML('11030239923', response.content.decode())
        self.assertNotIn('jose', response.content.decode())
        self.assertNotIn('11111111111', response.content.decode())

    # Read with filter
    def test_if_client_is_filtered_by_car_with_successful(self):
        response = self.client.get(
            reverse('client:list') + '?car_model=corsa'
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Jose', response.content.decode())
        self.assertInHTML('11111111111', response.content.decode())
        self.assertNotIn('Gustavo', response.content.decode())
        self.assertNotIn('11030239923', response.content.decode())

    # Read with filter
    def test_if_client_is_filtered_by_plate_with_successful(self):
        response = self.client.get(
            reverse('client:list') + '?plate=zzz-0000'
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Jose', response.content.decode())
        self.assertInHTML('11111111111', response.content.decode())
        self.assertNotIn('Gustavo', response.content.decode())
        self.assertNotIn('11939230072', response.content.decode())

    # Read with filter
    def test_if_client_is_filtered_by_date_with_successful(self):
        now = date.today()
        response = self.client.get(
            reverse('client:list') + f'?date={now}'
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Gustavo', response.content.decode())
        self.assertInHTML('11030239923', response.content.decode())

        yesterday = now - timedelta(days=1)
        response = self.client.get(
            reverse('client:list') + f'?date={yesterday}'
        )

        self.assertNotIn('Gustavo', response.content.decode())
        self.assertNotIn('11030239923', response.content.decode())

    # create
    def test_if_create_view_of_client_is_correct(self):

        data = {
            'client_name': 'Felipe',
            'cellphone': "(11) 99999-9999",
            'car_model': "sandero",
            'car_plate': "AAA-9999"
        }

        response = self.client.post(
            reverse('client:register'), data=data, follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Felipe', response.content.decode())
        self.assertInHTML('(11) 99999-9999', response.content.decode())
        self.assertInHTML('sandero', response.content.decode())
        self.assertInHTML('AAA-9999', response.content.decode())

    # Update
    def test_if_client_will_be_updated_with_success(self):

        response = self.client.post(
            reverse('client:update', args=(1,)),
            data={
                'client_name': 'José',
                'cellphone': "(11) 99999-9999",
                'car_model': "sandero",
                'car_plate': "AAA-9999"
            }
        )

        product = Client.objects.get(id=1)

        self.assertEqual(response.status_code, 302)
        self.assertIsNotNone(product)
        self.assertEqual(product.client_name, 'José')
        self.assertEqual(product.cellphone, '(11) 99999-9999')

    # Delete
    def test_if_client_will_be_deleted_with_successful(self):

        response = self.client.get(reverse('client:list'))
        self.assertInHTML('Gustavo', response.content.decode())
        self.assertEqual(response.status_code, 200)

        delete_item = self.client.post(
            reverse('client:delete', args=(1,))
        )

        self.assertEqual(delete_item.status_code, 302)
        self.assertNotIn('gustavo', delete_item.content.decode())
