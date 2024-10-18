from django.urls import path
from client import views

app_name = 'client'

urlpatterns = [
    path(
        'client/register/',
        views.RegisterClientView.as_view(),
        name="register"
    ),
    path(
        'client/register/loja',
        views.RegisterStoreView.as_view(),
        name="register_store"
    ),
    path(
        'client/<int:pk>/delete',
        views.DeleteClientView.as_view(),
        name="delete"
    ),
    
    path(
        'client/list/',
        views.ListClientView.as_view(),
        name="list"
    ),
    path(
        'client/<int:pk>/update',
        views.UpdateClientView.as_view(),
        name="update"
    ),
    path(
        'client/<int:pk>/delete',
        views.DeleteClientView.as_view(),
        name="delete"
    ),
]
