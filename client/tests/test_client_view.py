from django.test import TestCase
from django.urls import reverse
from client.models import Client


class TestClientView(TestCase):

    # read
    def test_if_list_view_client_function_with_success(self):
        Client.objects.create(
            client_name='gustavo',
            cellphone="11030239923",
            car_model="sandero",
            car_plate="asx-1030"
        )
        response = self.client.get(reverse('client:list'))

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Gustavo', response.content.decode())  # type:ignore

    # create
    def test_if_create_view_of_client_is_correct(self):

        data = {
            'client_name': 'felipe',
            'cellphone': '11392344429',
            'car_model': 'sandero',
            'car_plate': 'asx-1030'
        }

        response = self.client.post(
            reverse('client:register'), data=data, follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Felipe', response.content.decode())  # type:ignore
        self.assertInHTML('11392344429', response.content.decode())  # type:ignore
        self.assertInHTML('sandero', response.content.decode())  # type:ignore
        self.assertInHTML('asx-1030', response.content.decode())  # type:ignore

    # Update
    def test_if_client_will_be_updated_with_success(self):
        Client.objects.create(
            client_name='gustavo',
            cellphone="11030239923",
            car_model="sandero",
            car_plate="asx-1030"
        )

        response = self.client.post(
            reverse('client:update', args=(1,)),
            data={            
                'client_name': 'José',
                'cellphone': "11932933002",
                'car_model': "sandero",
                'car_plate': "asx-1030"
            }
        )

        product = Client.objects.get(id=1)

        self.assertEqual(response.status_code, 302)
        self.assertIsNotNone(product)
        self.assertEqual(product.client_name, 'José')
        self.assertEqual(product.cellphone, '11932933002')

    # Delete
    def test_if_client_will_be_deleted_with_successful(self):
        Client.objects.create(
            client_name='gustavo',
            cellphone="11030239923",
            car_model="sandero",
            car_plate="asx-1030"
        )

        response = self.client.get(reverse('client:list'))
        self.assertInHTML('Gustavo', response.content.decode())  # type:ignore
        self.assertEqual(response.status_code, 200)

        delete_item = self.client.post(
            reverse('client:delete', args=(1,))
        )

        self.assertEqual(delete_item.status_code, 302)
        self.assertNotIn('gustavo', delete_item.content.decode())
