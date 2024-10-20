from django.test import TestCase
from django.urls import reverse
from client.models import Client


class TestClientUrl(TestCase):
    def setUp(self) -> None:
        Client.objects.create(
            client_name='client_test', cellphone='11939239972',
        )
        return super().setUp()

    def test_if_url_of_create_client_return_200(self):
        response = self.client.get(reverse('client:register'))

        self.assertEqual(response.status_code, 200)

    def test_if_url_of_read_client_return_200(self):
        response = self.client.get(reverse('client:list'))

        self.assertEqual(response.status_code, 200)

    def test_if_url_of_update_client_return_200(self):
        response = self.client.get(reverse('client:update', args=(1,)))

        self.assertEqual(response.status_code, 200)

    def test_if_url_of_delete_client_return_200(self):
        response = self.client.get(reverse('client:delete', args=(1,)))

        self.assertEqual(response.status_code, 200)
