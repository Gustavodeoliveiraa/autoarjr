from service_order.models import ServiceOrder


def shortcut_create_service_order(
    client_name='teste__',
    client_cellphone='(11) 99999-9999',
    car_model='opala',
    car_plate='AAA-0000',
    service_price=200,
    service='service teste',
    paid=False,
    observation='',
    cpf='',
):
    ServiceOrder.objects.create(
        client_name=client_name, client_cellphone=client_cellphone,
        car_model=car_model, car_plate=car_plate, service_price=service_price,
        service=service, paid=paid, observation=observation, cpf=cpf
    )
