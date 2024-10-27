from account.forms import CustomerUserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy


class CreateUserView(CreateView):
    template_name = 'register.html'
    form_class = CustomerUserCreationForm
    success_url = reverse_lazy('account:login')


class CustomLoginVIew(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class LogoutUserView(LogoutView):
    template_name = 'delete.html'
