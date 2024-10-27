from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('account/register', views.CreateUserView.as_view(), name='register'),
    path('account/login', views.CustomLoginVIew.as_view(), name='login'),
    path('account/logout', views.LogoutView.as_view(), name='logout'),
]
