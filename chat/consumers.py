from contextlib import suppress
import json
from channels.generic.websocket import AsyncWebsocketConsumer

from projects.models import WebinarOnlineWatchersCount


class ChatConsumer(AsyncWebsocketConsumer):
    room_name = ''
    room_group_name = ''

    def get_counter(self):
        try:
            counter = WebinarOnlineWatchersCount.objects.get(webinar__pk=self.room_name)
            return counter
        except WebinarOnlineWatchersCount.DoesNotExist:
            return None

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        with suppress(WebinarOnlineWatchersCount.DoesNotExist):
            counter = self.get_counter()
            if counter and self.scope['user'].is_authenticated:
                counter.viewers.add(self.scope['user'])

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        counter = self.get_counter()
        if counter and self.scope['user'].is_authenticated:
            counter.viewers.remove(self.scope['user'])

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
