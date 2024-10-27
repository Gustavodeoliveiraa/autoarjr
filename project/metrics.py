from datetime import date, timedelta
from django.db.models import Sum
from service_order.models import ServiceOrder
from client.models import Client


def get_total_amount_of_cars_made():
    return ServiceOrder.objects.all().count()


def get_total_amount_of_cars_made_per_day_on_the_last_7_days():
    values = list()
    today = date.today()
    last_7_days = [(today - timedelta(days=i)) for i in range(6, -1, -1)]

    for day in last_7_days:
        value = ServiceOrder.objects.filter(created_at=day).count()

        values.append(float(value))

    return dict(
        data=[day.strftime('%A') for day in last_7_days],
        values=values
    )


def get_total_amount_selling():
    total_selling = ServiceOrder.objects.aggregate(total=Sum('service_price'))['total']

    return float(total_selling)


def get_total_amount_of_cps_registered():
    return ServiceOrder.objects.filter(cpf__isnull=False).exclude(cpf='').count()


def get_total_amount_of_clients_registered():
    return Client.objects.all().count()


def get_total_amount_of_made_on_week():
    values = list()
    today = date.today()
    date_ = [(today - timedelta(days=i))for i in range(6, -1, -1)]
    last_7_days = [(today - timedelta(days=i))for i in range(6, -1, -1)]

    for day in date_:
        sales_total = ServiceOrder.objects.filter(
            created_at=day
        ).aggregate(total=Sum('service_price'))['total'] or 0

        values.append(float(sales_total))

    return dict(
        dates=[day.strftime('%A') for day in last_7_days],
        values=values
    )


def get_total_quantity_of_cars_that_each_store_fix():
    all_store = [store.client_name for store in Client.objects.filter(is_store=True).exclude(is_store=False)]
    data = list()

    for store in all_store:
        value = ServiceOrder.objects.filter(client_name__iexact=store.strip()).count()
        data.append(value)

    return dict(
        all_store=all_store,
        values=data
    )
