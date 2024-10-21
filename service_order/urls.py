from django.urls import path
from service_order import views

app_name = 'service_order'

urlpatterns = [
    path(
        'service_order/register', views.RegisterServiceOrder.as_view(),
        name='register'
    ),
    path(
        '', views.ListServiceOrderView.as_view(),
        name='list'
    ),
    path(
        'service_order/<int:pk>/update', views.UpdateServiceOrderView.as_view(),
        name='update'
    ),
    path(
        'service_order/<int:pk>/delete', views.DeleteServiceOrderView.as_view(),
        name='delete'
    ),
    path(
        'service_order/<int:pk>/detail', views.DetailServiceOrderView.as_view(),
        name='detail'
    ),
    path(
        'service_order/<int:pk>/print', views.PrintServiceOrder.as_view(),
        name='print'
    ),

]
