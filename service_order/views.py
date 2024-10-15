from django.views import generic
from django.urls import reverse_lazy
from .models import ServiceOrder
from .forms import FormRegisterServiceOrder


class RegisterServiceOrder(generic.CreateView):
    model = ServiceOrder
    form_class = FormRegisterServiceOrder
    success_url = reverse_lazy('service_order:list')
    template_name = '../templates/register_service_order.html'


class ListServiceOrderView(generic.ListView):
    model = ServiceOrder
    context_object_name = 'service_orders'
    template_name = '../templates/list_service_order.html'

    def get_queryset(self):
        QuerySet = super().get_queryset()

        client_name = self.request.GET.get('client_name', '')
        client_cellphone = self.request.GET.get('client_cellphone', '')

        if client_name:
            QuerySet = QuerySet.filter(client_name__icontains=client_name)

        if client_cellphone:
            QuerySet = QuerySet.filter(
                client_cellphone__icontains=client_cellphone
            )

        car_model = self.request.GET.get('car_model', '')
        car_plate = self.request.GET.get('car_plate', '')
        paid = self.request.GET.get('paid', '')

        if car_model:
            QuerySet = QuerySet.filter(car_model__icontains=car_model)

        if car_plate:
            QuerySet = QuerySet.filter(car_plate__icontains=car_plate)

        if paid:
            QuerySet = (
                QuerySet.filter(paid=True) if paid == "1" else QuerySet.filter(paid=False) # noqa
            )

        return QuerySet


class UpdateServiceOrderView(generic.UpdateView):
    model = ServiceOrder
    form_class = FormRegisterServiceOrder
    success_url = reverse_lazy('service_order:list')
    template_name = '../templates/update_service_order.html'


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
