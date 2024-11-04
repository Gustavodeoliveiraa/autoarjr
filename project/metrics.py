import locale
import pytz
from datetime import datetime
from datetime import date, timedelta
from django.db.models import Sum, Count
from service_order.models import ServiceOrder
from client.models import Client

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


# metrics all
def get_total_quantity_of_cars_made():
    return ServiceOrder.objects.all().count()


def get_total_quantity_of_cps_registered():
    return ServiceOrder.objects.filter(cpf__isnull=False).exclude(cpf='').count()


def get_total_quantity_of_clients_registered():
    return Client.objects.all().count()


def get_total_amount_selling():
    total_selling = ServiceOrder.objects.aggregate(total=Sum('service_price'))['total']

    return float(total_selling) if total_selling is not None else 0.0
# end metrics all


# metrics of week
def get_today_and_one_week_ago():
    tz = pytz.timezone('America/Sao_Paulo')
    now = datetime.now(tz)  # Isso está correto
    today = now.date()
    one_week_ago = today - timedelta(days=6)

    return [today, one_week_ago]


def get_total_quantity_of_car_made_on_week():
    today, one_week_ago = get_today_and_one_week_ago()
    total_values = ServiceOrder.objects.filter(created_at__range=[one_week_ago, today]).count()

    return total_values


def get_total_quantity_of_clients_registered_on_week():
    today, one_week_ago = get_today_and_one_week_ago()

    values = Client.objects.filter(created_at__range=[one_week_ago, today]).count()
    return values


def get_total_amount_of_selling_on_week():
    today, one_week_ago = get_today_and_one_week_ago()

    values = ServiceOrder.objects.filter(
        created_at__range=[one_week_ago, today]
    ).aggregate(total=Sum('service_price'))['total']

    return values or 0
# end metrics of week


# chart metrics of wek
def get_total_amount_made_per_day_on_week():
    today, one_week_ago = get_today_and_one_week_ago()
    date_list = [(today - timedelta(days=i)) for i in range(6, -1, -1)]

    sales_total = ServiceOrder.objects.filter(
        created_at__range=[one_week_ago, today]
    ).values('created_at').annotate(total=Sum('service_price')).order_by('created_at')

    daily_totals = {sales['created_at']: float(sales['total']) or 0 for sales in sales_total}

    return dict(
        dates=[day.strftime('%A') for day in date_list],
        values=[daily_totals.get(day, 0) for day in date_list]
    )


def get_total_quantity_of_cars_made_per_day_on_week():
    today, one_week_ago = get_today_and_one_week_ago()
    last_7_days = [(today - timedelta(days=i)) for i in range(6, -1, -1)]

    daily_quantity = ServiceOrder.objects.filter(
        created_at__range=[one_week_ago, today]
    ).values('created_at').annotate(total=Count('id'))

    daily_totals = {entry['created_at']: entry['total'] for entry in daily_quantity}

    values = [daily_totals.get(day, 0) for day in last_7_days]

    return dict(
        data=[day.strftime('%A') for day in last_7_days],
        values=values
    )


def get_total_quantity_of_cars_that_each_store_fix():
    store_data = ServiceOrder.objects.filter(
        client_name__in=Client.objects.filter(
            is_store=True
        ).values_list(
            'client_name', flat=True
        )
    ).values('client_name').annotate(total_cars_fixed_count=Count('id'))

    return dict(
        all_store=[data['client_name'] for data in store_data],
        values=[data['total_cars_fixed_count'] for data in store_data]
    )
# end chart metrics of week
