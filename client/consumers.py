# type: ignore
import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ClientUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Conectando WebSocket...")
        self.room_group_name = "client_update_room"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        print("WebSocket Conectado.")

    async def disconnect(self, close_code):
        print("Desconectando WebSocket...")
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def notify_update(self, event):
        print("Notificando atualização: ", event["action"])
        await self.send(text_data=json.dumps({
            "action": event["action"],
        }))