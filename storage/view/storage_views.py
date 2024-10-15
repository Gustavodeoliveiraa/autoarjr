from ..models import Storage, CategoryStorage
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView
)
from ..forms import StorageForm


class RegisterStorage(CreateView):
    model = Storage
    template_name = '../templates/storage/create_storage.html'
    success_url = reverse_lazy('storage:storage_list')
    form_class = StorageForm
    template_name_suffix = 'storage'


class ListStorageView(ListView):
    model = Storage
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


class DetailStorageView(DetailView):
    model = Storage
    context_object_name = 'product'
    template_name = '../templates/storage/detail_storage.html'


class UpdateStorageView(UpdateView):
    model = Storage
    form_class = StorageForm
    template_name = '../templates/storage/update_storage.html'
    success_url = reverse_lazy('storage:storage_list')


class DeleteStorageView(DeleteView):
    model = Storage
    template_name = '../templates/storage/delete_storage.html'
    success_url = reverse_lazy('storage:storage_list')
