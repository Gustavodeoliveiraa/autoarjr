from django import forms
from .models import Storage, CategoryStorage


class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['name', 'quantity', 'category', 'detail']

        labels = {
            'name': 'Nome',
            'quantity': 'Quantidade',
            'category': 'Categoria',
            'detail': 'Detalhes'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs['class'] = 'form-control'


class CategoryForm(forms.ModelForm):

    class Meta:
        model = CategoryStorage
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {'name': 'Nome'}
