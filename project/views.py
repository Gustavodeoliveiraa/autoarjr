from django.views import View
from django.shortcuts import render
from project import metrics


class DashBoardView(View):
    template_name = '../templates/metrics/dashboard.html'

    def get(self, request):
        data = {
            'total_of_cars_made': metrics.get_total_amount_of_cars_made(),
            'total_selling': metrics.get_total_amount_selling(),
            'total_cpf_registered': metrics.get_total_amount_of_cps_registered(),
            'total_clients_registered': metrics.get_total_amount_of_clients_registered(),

            'total_value_of_sales_for_day_of_week': metrics.get_total_amount_of_made_on_week(),
            'sales_by_day_of_the_week': metrics.get_total_amount_of_cars_made_per_day_on_the_last_7_days(),
            'quantity_of_cars_that_each_store_fix': metrics.get_total_quantity_of_cars_that_each_store_fix()
        }

        return render(request, self.template_name, data)
