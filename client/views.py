from django.views import generic
from .models import Client
from .forms import FormClient
from django.urls import reverse_lazy


class RegisterClientView(generic.CreateView):
    model = Client
    form_class = FormClient
    template_name = '../templates/create_client.html'
    success_url = reverse_lazy('client:list')


class ListClientView(generic.ListView):
    model = Client
    template_name = '../templates/list_client.html'
    context_object_name = 'clients'

    def get_queryset(self):
        querySet = super().get_queryset()

        car_name = self.request.GET.get('name', '').strip()
        if car_name:
            querySet = querySet.filter(client_name__icontains=car_name)

        cellphone = self.request.GET.get('cellphone', '').strip()
        if cellphone:
            querySet = querySet.filter(cellphone__icontains=cellphone)

        car_model = self.request.GET.get('car_model', '').strip()
        if car_model:
            querySet = querySet.filter(car_model__icontains=car_model)

        car_plate = self.request.GET.get('plate', '').strip()
        if car_plate:
            querySet = querySet.filter(car_plate__icontains=car_plate)

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
