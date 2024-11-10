from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestUserPermissions(TestCase):

    def tests_if_user_access_is_denied_without_permission(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def tests_if_user_access_is_allowed_with_permission(self):
        User.objects.create_user(username='user1', password='password1', is_staff=True)

        self.client.login(username='user1', password='password1')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_if_user_not_authenticated_will_be_redirect_for_login_page(self):
        User.objects.create_user(username='user1', password='password1', is_staff=False)

        self.client.login(username='user1', password='password1')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
