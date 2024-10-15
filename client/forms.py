import re
from django import forms
from .models import Client


class FormClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'cellphone', 'car_model', 'car_plate']
        labels = {
            'client_name': 'Nome',
            'cellphone': 'Telefone',
            'car_model': 'Carro',
            'car_plate': 'Placa do Veiculo'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            field = self.fields[field]
            field.widget.attrs['class'] = 'form-control'

        self.fields['car_plate'].widget.attrs['id'] = 'id_car_plate'
        self.fields['cellphone'].widget.attrs['id'] = 'cellphone'

    def clean_cellphone(self):
        cellphone = self.cleaned_data['cellphone']

        if not re.match(r'^\(\d{2}\) \d{5}-\d{4}$', cellphone):
            raise forms.ValidationError("Por favor, insira um número de telefone válido no formato (11) 99999-9999.")
        return cellphone

    def clean_car_plate(self):
        plate = self.cleaned_data.get('car_plate')

        old_plate_pattern = r'^[A-Z]{3}-\d{4}$'
        new_plate_pattern = r'^[A-Z]{3}\d[A-Z]\d{2}$'

        if not (re.match(old_plate_pattern, plate) or re.match(new_plate_pattern, plate)):  # type: ignore
            raise forms.ValidationError('A placa deve estar no formato válido: AAA-9999 ou AAA9A99.')

        return plate
