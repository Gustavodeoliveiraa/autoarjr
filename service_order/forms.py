import re
from django.forms import ModelForm
from django import forms
from .models import ServiceOrder, Services


class FormRegisterServiceOrder(ModelForm):
    service1 = forms.ModelMultipleChoiceField(
        queryset=Services.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = ServiceOrder
        fields = [
            'client_name', 'client_cellphone', 'car_model',
            'car_plate', 'service1', 'service_price', 'observation', 'paid',
            'cpf'
        ]
        labels = {
            'client_name': 'Nome do Cliente',
            'client_cellphone': 'Telefone',
            'car_model': 'Carro',
            'car_plate': 'Placa',
            'service_price': 'Valor do Serviço',
            'service': 'Serviço feito',
            'service1': 'Serviço feito',
            'paid': 'Pago',
            'observation': 'Observações',
            'cpf': 'CPF / CNPJ'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs['class'] = 'form-control'

        self.fields['paid'].widget.attrs['class'] = 'form-check-input ms-3 me-3'
        self.fields['paid'].help_text = 'Marque se o pagamento foi realizado.'
        self.fields['car_plate'].widget.attrs['id'] = 'id_car_plate'
        self.fields['client_cellphone'].widget.attrs['id'] = 'cellphone'
        self.fields['cpf'].widget.attrs['id'] = 'cpf'
        self.fields['service1'].widget.attrs['class'] = ''

    def clean_client_cellphone(self):
        cellphone = self.cleaned_data['client_cellphone']

        if not re.match(r'^\(\d{2}\) \d{5}-\d{4}$', cellphone):
            raise forms.ValidationError(
                "Por favor, insira um número de telefone \
                    válido no formato (11) 99999-9999."
            )
        return cellphone

    def clean_car_plate(self):
        plate = self.cleaned_data.get('car_plate')

        old_plate_pattern = r'^[A-Z]{3}-\d{4}$'
        new_plate_pattern = r'^[A-Z]{3}\d[A-Z]\d{2}$'

        if not (re.match(old_plate_pattern, plate) or re.match(new_plate_pattern, plate)):  # type: ignore
            raise forms.ValidationError(
                'A placa deve estar no formato válido: AAA-9999 ou AAA9A99.'
            )

        return plate
