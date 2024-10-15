from django.urls import path
from .view.storage_views import (
    RegisterStorage, ListStorageView, DetailStorageView, UpdateStorageView,
    DeleteStorageView
)
from .view.category_views import (
    RegisterCategory, ListCategories, DeleteCategory, UpdateCategory
)

app_name = 'storage'

urlpatterns = [
    # storage
    path('storage/create/', RegisterStorage.as_view(), name='storage_create'),
    path('storage/list/', ListStorageView.as_view(), name='storage_list'),
    path(
        'storage/<int:pk>/detail/',
        DetailStorageView.as_view(),
        name='storage_detail'
    ),
    path(
        'storage/<int:pk>/update/',
        UpdateStorageView.as_view(),
        name='storage_update'
    ),
    path(
        'storage/<int:pk>/delete/',
        DeleteStorageView.as_view(),
        name='storage_delete'
    ),

    # category
    path('category/create/', RegisterCategory.as_view(), name='create_category'),
    path('category/list/', ListCategories.as_view(), name='list_category'),
    path(
        'category/<int:pk>/delete/',
        DeleteCategory.as_view(),
        name='delete_category'
    ),
    path(
        'category/<int:pk>/delete/',
        DeleteCategory.as_view(),
        name='delete_category',
    ),

    path(
        'category/<int:pk>/update/',
        UpdateCategory.as_view(),
        name='update_category',
    ),

]
