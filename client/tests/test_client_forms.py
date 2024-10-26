from django.test import TestCase
from django.urls import reverse
from client.forms import FormClient, FormRegisterLoja


class TestFormStore(TestCase):

    def test_if_form_store_save_with_is_store_be_false(self):
        data = {'client_name': 'jose'}
        form = FormRegisterLoja(data)

        if not form.is_valid():
            print("Erros de validação:", form.errors)

        self.assertTrue(form.is_valid())

        store_instance = form.save(commit=True)
        self.assertTrue(store_instance.is_store)


class TestFormClient(TestCase):
    def test_if_form_client_save_with_is_store_be_false(self):
        data = {
            'client_name': 'teste001',
            'cellphone': '(00) 00000-0000',
            'car_model': 'fusca',
            'car_plate': 'FFX-2990'
        }

        form = FormClient(data)
        if not form.is_valid():
            print('Erros de validação:', form.errors)

        self.assertTrue(form.is_valid())

        client_instance = form.save(commit=True)
        self.assertFalse(client_instance.is_store)
