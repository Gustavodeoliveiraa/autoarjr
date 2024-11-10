# type:ignore
from django.test import TestCase
from django.urls import reverse
from client.models import Client
from django.contrib.auth.models import Permission, User


class TestAllPermissionsOfTheClientView(TestCase):
    def setUp(self) -> None:
        self.regular_user = User.objects.create_user(username='regular', password='password', is_staff=False)
        self.staff_user = User.objects.create_superuser(username='super', email='', password='password')

        return super().setUp()

    def test_permissions_denied_for_register_client_view(self):
        self.client.login(username='regular', password='password')
        response = self.client.get(reverse('client:register'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Você não tem permissão para registrar clientes")

    def test_permission_allowed_for_register_client_view(self):
        permissions = Permission.objects.filter(
            codename__in=['add_client', 'change_client', 'delete_client']
        )
        self.regular_user.user_permissions.set(permissions)

        self.user = User.objects.get(username='regular')
        self.user.refresh_from_db()

        self.assertTrue(self.user.has_perm('client.add_client'))
        self.assertTrue(self.user.has_perm('client.change_client'))
        self.assertTrue(self.user.has_perm('client.delete_client'))

        # Try to log in and access the client registration page
        self.client.login(username='regular', password='password')
        response = self.client.get(reverse('client:register'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Cadastrar Cliente', response.content.decode())

    def test_permission_denied_for_register_store(self):
        self.user = self.regular_user

        self.assertFalse(self.user.has_perm('client.add_client'))
        self.assertFalse(self.user.has_perm('client.change_client'))
        self.assertFalse(self.user.has_perm('client.delete_client'))

        # Try to log in and access the client registration page
        self.client.login(username='regular', password='password')
        response = self.client.get(reverse('client:register'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertInHTML("Você não tem permissão para registrar clientes", response.content.decode())

    def test_permission_allowed_for_register_store(self):
        permissions = Permission.objects.filter(
            codename__in=['add_client', 'change_client', 'delete_client']
        )
        self.regular_user.user_permissions.set(permissions)
        self.user = User.objects.get(username='regular')
        self.user.refresh_from_db()

        self.assertTrue(self.user.has_perm('client.add_client'))
        self.assertTrue(self.user.has_perm('client.change_client'))
        self.assertTrue(self.user.has_perm('client.delete_client'))

        # Try to log in and access the client registration page
        self.client.login(username='regular', password='password')
        response = self.client.get(reverse('client:register'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Cadastrar Cliente', response.content.decode())

    def test_permission_denied_for_change_data_of_clients(self):
        self.client.login(username='regular', password='password')
        user = User.objects.get(username='regular')
        self.assertFalse(user.has_perm('client.change.client'))

        response = self.client.get(reverse('client:update', args=(1,)), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertInHTML("Você não tem permissão para atualizar clientes", response.content.decode())

    def test_permission_allowed_for_change_client(self):
        # make one client for access the her url after
        Client.objects.create(client_name='teste')

        permission = Permission.objects.get(codename='change_client')
        self.regular_user.user_permissions.add(permission)
        user = User.objects.get(username='regular')

        self.assertTrue(user.has_perm('client.change_client'))

        user.refresh_from_db()
        self.client.login(username='regular', password='password')

        response = self.client.get(reverse('client:update', args=(1,)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertInHTML("Atualizar Cliente", response.content.decode())

    def test_permission_denied_for_delete_client(self):
        self.client.login(username='regular', password='password')
        user = User.objects.get(username='regular')
        self.assertFalse(user.has_perm('client.delete.client'))

        response = self.client.get(reverse('client:delete', args=(1,)), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertInHTML("Você não tem permissão para deletar clientes", response.content.decode())

    def test_permission_allowed_for_delete_client(self):
        Client.objects.create(client_name='teste')

        permission = Permission.objects.get(codename='delete_client')
        self.regular_user.user_permissions.add(permission)
        self.regular_user.refresh_from_db()

        user = Client.objects.get(client_name='teste')
        self.assertIsNotNone(user)

        self.client.login(username='regular', password='password')
        response = self.client.post(reverse('client:delete', args=(1,)), follow=True)
        self.assertEqual(response.status_code, 200)

        with self.assertRaises(Client.DoesNotExist):
            user = Client.objects.get(client_name='teste')
