# type: ignore

from django.test import TestCase
from django.urls import reverse
from storage.models import CategoryStorage
from django.test import Client as TestClient
from django.contrib.auth.models import User


class TestCategoryView(TestCase):

    def setUp(self) -> None:

        self.user = User.objects.create_superuser(username='gustavo', password='12345')
        self.client = TestClient()
        self.client.login(username='gustavo', password='12345')
        self.client.post(
            reverse('storage:create_category'),
            data={
                'name': 'condensador'
            }
        )
        return super().setUp()

    # create
    def test_if_category_is_created_with_success(self):
        response = self.client.post(
            reverse('storage:create_category'),
            data={
                'name': 'compressor'
            }
        )

        category = CategoryStorage.objects.get(name='compressor')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(category.name, 'compressor')

    # read
    def test_if_category_list_view_function_with_success(self):
        response = self.client.get(reverse('storage:list_category'))

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('condensador', response.content.decode())

    def test_if_category_will_be_filtered_by_name(self):
        CategoryStorage.objects.create(name='compressor')
        response = self.client.get(
            reverse('storage:list_category') + '?name=compressor'
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('compressor', response.content.decode())
        self.assertNotIn('condensador', response.content.decode())

    # update
    def test_if_category_is_updated_with_success(self):
        data = {'name': 'um_teste'}

        response = self.client.post(
            reverse('storage:update_category', args=(1,)),
            data=data
        )

        category = CategoryStorage.objects.filter(name=data['name']).first()
        self.assertIsNotNone(category)
        self.assertEqual(category.name, data['name'])
        self.assertEqual(response.status_code, 302)

    # delete
    def test_if_category_is_deleted_with_success(self):
        response = self.client.post(
            reverse('storage:delete_category', args=(1,))
        )

        category = CategoryStorage.objects.filter(pk=1).first()

        self.assertIsNone(category)
        self.assertEqual(response.status_code, 302)
