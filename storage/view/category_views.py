from django.db.models.query import QuerySet
from ..models import CategoryStorage
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from ..forms import CategoryForm


class RegisterCategory(CreateView):
    model = CategoryStorage
    form_class = CategoryForm
    template_name = '../templates/category/create_category.html'
    success_url = reverse_lazy('storage:list_category')


class ListCategories(ListView):
    model = CategoryStorage
    context_object_name = 'items'
    template_name = '../templates/category/list_category.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.request.GET.get('name')

        if category_name:
            print('rapaz')
            queryset = queryset.filter(name__icontains=category_name)
        return queryset


class DeleteCategory(DeleteView):
    model = CategoryStorage
    template_name = '../templates/category/delete_category.html'
    success_url = reverse_lazy('storage:list_category')


class UpdateCategory(UpdateView):
    model = CategoryStorage
    form_class = CategoryForm
    template_name = '../templates/category/update_category.html'
    success_url = reverse_lazy('storage:list_category')
