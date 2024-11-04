from django.views import View
from django.shortcuts import render, redirect
from project import metrics
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


class DashBoardView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = '../templates/metrics/dashboard.html'
    permission_denied_message = 'Você não tem permissão para acessar essa pagina'

    def test_func(self):
        return self.request.user.is_staff  # type: ignore

    def handle_no_permission(self):
        messages.warning(self.request, self.permission_denied_message)
        return redirect('service_order:list')

    def get(self, request):
        data = {
            # total metrics
            'total_of_cars_made': metrics.get_total_quantity_of_cars_made(),
            'total_cpf_registered': metrics.get_total_quantity_of_cps_registered(),
            'total_clients_registered': metrics.get_total_quantity_of_clients_registered(),
            'total_selling': metrics.get_total_amount_selling(),
            # end total metrics

            # metrics of week
            'total_of_cars_made_on_week': metrics.get_total_quantity_of_car_made_on_week(),
            'total_of_clients_registered_on_week': metrics.get_total_quantity_of_clients_registered_on_week(),
            'total_amount_of_selling_on_week': metrics.get_total_amount_of_selling_on_week(),
            # end metrics of week


            # metrics of week  (chart)
            'total_value_of_sales_per_day_on_week': metrics.get_total_amount_made_per_day_on_week(),
            'sales_by_day_of_the_week': metrics.get_total_quantity_of_cars_made_per_day_on_week(),
            'quantity_of_cars_that_each_store_fix': metrics.get_total_quantity_of_cars_that_each_store_fix()
            # end metrics of week  (chart)

        }

        return render(request, self.template_name, data)
