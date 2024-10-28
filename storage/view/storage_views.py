from ..models import Storage, CategoryStorage
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView
)
from ..forms import StorageForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class RegisterStorage(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Storage
    template_name = '../templates/storage/create_storage.html'
    success_url = reverse_lazy('storage:storage_list')
    form_class = StorageForm
    template_name_suffix = 'storage'
    permission_required = 'storage.add_storage'
    permission_denied_message = 'Você não tem permissão para cadastrar no estoque'

    def handle_no_permission(self):
        messages.warning(self.request, self.permission_denied_message)
        return redirect('storage:storage_list')


class ListStorageView(LoginRequiredMixin, ListView):
    model = Storage
    paginate_by = 10
    context_object_name = 'products'
    template_name = '../templates/storage/list_storage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryStorage.objects.all()

        return context

    def get_queryset(self):
        querySet = super().get_queryset()

        name = self.request.GET.get('name')
        if name:
            querySet = querySet.filter(name__icontains=name)

        category = self.request.GET.get('category')

        if category:
            querySet = querySet.filter(category_id=category)

        return querySet


class DetailStorageView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Storage
    context_object_name = 'product'
    template_name = '../templates/storage/detail_storage.html'
    permission_required = 'storage.view_storage'
    permission_denied_message = 'Você não tem permissão para visualizar este item'

    def handle_no_permission(self):
        messages.warning(self.request, self.permission_denied_message)
        return redirect('storage:storage_list')


class UpdateStorageView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Storage
    form_class = StorageForm
    template_name = '../templates/storage/update_storage.html'
    success_url = reverse_lazy('storage:storage_list')
    permission_required = 'storage.change_storage'
    permission_denied_message = 'Você não tem permissão para atualizar este item'

    def handle_no_permission(self):
        messages.warning(self.request, self.permission_denied_message)
        return redirect('storage:storage_list')


class DeleteStorageView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Storage
    template_name = '../templates/storage/delete_storage.html'
    success_url = reverse_lazy('storage:storage_list')
    permission_required = 'storage.delete_storage'
    permission_denied_message = 'Você não tem permissão para deletar este item'

    def handle_no_permission(self):
        messages.warning(self.request, self.permission_denied_message)
        return redirect('storage:storage_list')
