from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from .models import ServiceOrder
from .forms import FormRegisterServiceOrder
from utils.remove_item_of_storage import rm_item_of_storage
from utils.get_stripped_value import (
    get_and_strip_request_param as strip_param
)
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class RegisterServiceOrder(PermissionRequiredMixin, LoginRequiredMixin, generic.CreateView):
    model = ServiceOrder
    form_class = FormRegisterServiceOrder
    success_url = reverse_lazy('service_order:list')
    template_name = '../templates/register_service_order.html'
    permission_required = 'service_order.add_serviceorder'
    permission_denied_message = 'Você não tem permissão para criar ordens de serviço !'

    def handle_no_permission(self):
        messages.warning(self.request, self.permission_denied_message)
        return redirect('service_order:list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)


class ListServiceOrderView(LoginRequiredMixin, generic.ListView):
    model = ServiceOrder
    paginate_by = 25
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
        filters = {key: value for key, value in filters.items() if value}

        paid = strip_param(self, 'paid')
        if paid:
            filters['paid'] = True if paid == "1" else False  # type: ignore

        QuerySet = QuerySet.filter(**filters) if filters else QuerySet
        return QuerySet


class UpdateServiceOrderView(PermissionRequiredMixin, LoginRequiredMixin, generic.UpdateView):
    model = ServiceOrder
    form_class = FormRegisterServiceOrder
    success_url = reverse_lazy('service_order:list')
    template_name = '../templates/update_service_order.html'
    permission_required = 'service_order.change_serviceorder'
    permission_denied_message = 'Você não tem permissão para atualizar ordens de serviço !'

    def handle_no_permission(self):
        messages.warning(self.request, self.permission_denied_message)
        return redirect('service_order:list')


class DetailServiceOrderView(PermissionRequiredMixin, LoginRequiredMixin, generic.DetailView):
    model = ServiceOrder
    context_object_name = 'service_order'
    template_name = '../templates/detail_service_order.html'
    permission_required = 'service_order.view_serviceorder'
    permission_denied_message = 'Você não tem permissão para visualizar ordens de serviço !'

    def handle_no_permission(self):
        messages.warning(self.request, self.permission_denied_message)
        return redirect('service_order:list')


class DeleteServiceOrderView(PermissionRequiredMixin, LoginRequiredMixin, generic.DeleteView):
    model = ServiceOrder
    success_url = reverse_lazy('service_order:list')
    template_name = '../templates/delete_service_order.html'
    permission_required = 'service_order.delete_serviceorder'
    permission_denied_message = 'Você não tem permissão para deletar ordens de serviço !'

    def handle_no_permission(self):
        messages.warning(self.request, self.permission_denied_message)
        return redirect('service_order:list')


class PrintServiceOrder(LoginRequiredMixin, generic.DetailView):
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
