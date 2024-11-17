# type: ignore
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def notify_clients(action):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "client_update_room",  # Nome do grupo
        {
            "type": "notify_update",  # Correspondente ao método notify_update no consumidor
            "action": action,        # Ação realizada: 'created', 'updated', etc.
        },
    )