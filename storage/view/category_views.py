from ..models import CategoryStorage
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from ..forms import CategoryForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class RegisterCategory(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = CategoryStorage
    form_class = CategoryForm
    template_name = '../templates/category/create_category.html'
    success_url = reverse_lazy('storage:list_category')
    permission_required = 'storage.add_categorystorage'
    permission_denied_message = 'Você não tem permissão para criar categorias'

    def handle_no_permission(self):
        messages.warning(self.request, self.permission_denied_message)
        return redirect('storage:list_category')


class ListCategories(LoginRequiredMixin, ListView):
    model = CategoryStorage
    paginate_by = 10
    context_object_name = 'items'
    template_name = '../templates/category/list_category.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.request.GET.get('name')

        if category_name:
            print('rapaz')
            queryset = queryset.filter(name__icontains=category_name)
        return queryset


class DeleteCategory(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = CategoryStorage
    template_name = '../templates/category/delete_category.html'
    success_url = reverse_lazy('storage:list_category')
    permission_required = 'storage.delete_categorystorage'
    permission_denied_message = 'Você não tem permissão para deletar categorias'

    def handle_no_permission(self):
        messages.warning(self.request, self.permission_denied_message)
        return redirect('storage:list_category')


class UpdateCategory(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = CategoryStorage
    form_class = CategoryForm
    template_name = '../templates/category/update_category.html'
    success_url = reverse_lazy('storage:list_category')
    permission_required = 'storage.change_categorystorage'
    permission_denied_message = 'Você não tem permissão para atualizar categorias'

    def handle_no_permission(self):
        messages.warning(self.request, self.permission_denied_message)
        return redirect('storage:list_category')