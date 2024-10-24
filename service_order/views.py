from django.views import generic
from django.urls import reverse_lazy
from .models import ServiceOrder, Services, ServiceCategory
from .forms import FormRegisterServiceOrder
from utils.get_stripped_value import (
    get_and_strip_request_param as strip_param
)


class RegisterServiceOrder(generic.CreateView):
    model = ServiceOrder
    form_class = FormRegisterServiceOrder
    success_url = reverse_lazy('service_order:list')
    template_name = '../templates/register_service_order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service1'] = Services.objects.all()
        context['categories'] = ServiceCategory.objects.all()
        return context


class ListServiceOrderView(generic.ListView):
    model = ServiceOrder
    context_object_name = 'service_orders'
    template_name = '../templates/list_service_order.html'

    def get_queryset(self):
        QuerySet = super().get_queryset()

        filters = {
            'client_name__icontains': strip_param(self, 'client_name'),
            'client_cellphone__icontains': strip_param(self, 'client_cellphone'),
            'car_model__icontains': strip_param(self, 'car_model'),
            'car_plate__icontains': strip_param(self, 'car_plate'),
            'created_at__icontains': strip_param(self, 'date')
        }

        # remove empty values
        filters = {key: value for key, value in filters.items() if key}

        paid = strip_param(self, 'paid')
        if paid:
            filters['paid'] = True if paid == "1" else False  # type: ignore

        QuerySet = QuerySet.filter(**filters) if filters else QuerySet
        return QuerySet


class UpdateServiceOrderView(generic.UpdateView):
    model = ServiceOrder
    form_class = FormRegisterServiceOrder
    success_url = reverse_lazy('service_order:list')
    template_name = '../templates/update_service_order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service1'] = Services.objects.all()
        context['categories'] = ServiceCategory.objects.all()
        return context


class DetailServiceOrderView(generic.DetailView):
    model = ServiceOrder
    context_object_name = 'service_order'
    template_name = '../templates/detail_service_order.html'


class DeleteServiceOrderView(generic.DeleteView):
    model = ServiceOrder
    success_url = reverse_lazy('service_order:list')
    template_name = '../templates/delete_service_order.html'


class PrintServiceOrder(generic.DetailView):
    model = ServiceOrder
    context_object_name = 'service_order'
    template_name = '../templates/print_service_order.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        service_order = self.object  # type: ignore
        context['service'] = service_order.service

        list_service = list()
        all_services = context['service'].split(',')
        [list_service.append(service) for service in all_services]

        while len(list_service) < 14:
            list_service.append('')

        context['filtered_service'] = list_service

        return context
