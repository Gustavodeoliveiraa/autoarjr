from django.test import TestCase
from django.urls import reverse
from storage.models import Storage, CategoryStorage


class TestCreateStorage(TestCase):

    def setUp(self) -> None:
        self.category = CategoryStorage.objects.create(name='compressor')
        self.category2 = CategoryStorage.objects.create(name='valvula')
        return super().setUp()

    # Create
    def test_if_storage_is_created_with_success(self):
        response = self.client.post(
            reverse('storage:storage_create'),
            data={
                'name': 'rele',
                'quantity': '2',
                'category': self.category.pk
            }
        )

        product = Storage.objects.filter(name='rele').first()
        self.assertIsNotNone(product)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(product.name, 'rele')  # type: ignore

    # Filter by name
    def test_if_products_will_be_filtered_per_name_with_successful(self):
        Storage.objects.create(
            name='valvula', quantity=2, category=self.category
        )
        Storage.objects.create(name='rele', quantity=1, category=self.category)

        response = self.client.get(
            reverse('storage:storage_list') + '?name=valvula'
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('valvula', response.content.decode())  # type: ignore
        self.assertInHTML('2', response.content.decode())  # type: ignore
        self.assertNotIn('rele', response.content.decode())

    # Filter by category
    def test_if_product_will_be_filtered_per_category_with_successful(self):
        Storage.objects.create(
            name='valvula', quantity=2, category=self.category2
        )
        Storage.objects.create(
            name='rele', quantity=1, category=self.category
        )

        response = self.client.get(
            reverse('storage:storage_list') + f'?category={self.category2.pk}'
        )

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('valvula', response.content.decode())  # type: ignore
        self.assertNotIn('rele', response.content.decode())

    # Update
    def test_if_product_will_be_updated_with_successful(self):
        Storage.objects.create(name='rele', quantity=1, category=self.category)

        response = self.client.post(
            reverse('storage:storage_update', args=(1,)),
            data={'name': 'fusivel', 'quantity': 2, "category": 1}
        )
        product = Storage.objects.get(id=1)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(product.name, 'fusivel')
        self.assertNotEqual(product.name, 'rele')

    # Delete
    def test_if_product_will_be_deleted_with_successful(self):
        Storage.objects.create(name='rele', quantity=1, category=self.category)

        response = self.client.post(
            reverse('storage:storage_delete', args=(1,))
        )

        product = Storage.objects.filter(id=1).first()
        self.assertEqual(response.status_code, 302)
        self.assertIsNone(product)
