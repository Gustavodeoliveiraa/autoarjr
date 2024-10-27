from django.views import generic
from .models import Client
from .forms import FormClient, FormRegisterLoja
from django.urls import reverse_lazy
from utils.get_stripped_value import (
    get_and_strip_request_param as strip_param
)


class RegisterClientView(generic.CreateView):
    model = Client
    form_class = FormClient
    template_name = '../templates/create_client.html'
    success_url = reverse_lazy('client:list')


class RegisterStoreView(generic.CreateView):
    model = Client
    form_class = FormRegisterLoja
    template_name = '../templates/create_client.html'
    success_url = reverse_lazy('client:list')


class ListClientView(generic.ListView):
    model = Client
    paginate_by = 25
    template_name = '../templates/list_client.html'
    context_object_name = 'clients'

    def get_queryset(self):
        querySet = super().get_queryset()

        car_name = strip_param(self, 'name')
        if car_name:
            querySet = querySet.filter(client_name__icontains=car_name)

        cellphone = strip_param(self, 'cellphone')
        if cellphone:
            querySet = querySet.filter(cellphone__icontains=cellphone)

        car_model = strip_param(self, 'car_model')
        if car_model:
            querySet = querySet.filter(car_model__icontains=car_model)

        car_plate = strip_param(self, 'plate')
        if car_plate:
            querySet = querySet.filter(car_plate__icontains=car_plate)

        date_time = strip_param(self, 'date')
        if date_time:
            querySet = querySet.filter(created_at=date_time)
        return querySet


class UpdateClientView(generic.UpdateView):
    model = Client
    form_class = FormClient
    template_name = '../templates/update_client.html'
    success_url = reverse_lazy('client:list')


class DeleteClientView(generic.DeleteView):
    model = Client
    template_name = '../templates/delete_client.html'
    success_url = reverse_lazy('client:list')
