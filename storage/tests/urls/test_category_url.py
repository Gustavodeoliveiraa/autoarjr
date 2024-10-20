from django.test import TestCase
from django.urls import reverse
from storage.models import CategoryStorage


class TestCategoryURL(TestCase):

    def setUp(self) -> None:
        self.category = CategoryStorage.objects.create(name='fist category')
        return super().setUp()

    def test_if_url_of_create_category_return_200(self):
        response = self.client.get(reverse('storage:create_category'))
        self.assertEqual(response.status_code, 200)

    def test_if_url_of_list_category_return_200(self):
        response = self.client.get(reverse('storage:list_category'))
        self.assertEqual(response.status_code, 200)

    def test_if_url_of_update_category_return_200(self):
        response = self.client.get(
            reverse('storage:update_category', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 200)

    def test_if_url_of_delete_category_return_200(self):
        response = self.client.get(reverse('storage:delete_category', args=(1,)))
        self.assertEqual(response.status_code, 200)
