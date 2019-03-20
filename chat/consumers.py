import asyncio
import datetime
import json
from math import floor, ceil
from random import randint

from channels.generic.websocket import AsyncWebsocketConsumer

from .models import ChatMessage
from projects.models import WebinarOnlineWatchersCount, Webinar


class ChatConsumer(AsyncWebsocketConsumer):
    room_name = ''
    room_group_name = ''
    counter = None
    webinar = None

    def get_counter(self):
        try:
            counter = WebinarOnlineWatchersCount.objects.get(webinar__pk=self.room_name)
        except WebinarOnlineWatchersCount.DoesNotExist:
            counter = None
        return counter

    def get_webinar(self):
        try:
            webinar = Webinar.objects.get(pk=self.room_name)
        except Webinar.DoesNotExist:
            webinar = None
        return webinar

    @staticmethod
    def get_fake_count(start_point, values_range):
        if start_point not in values_range:
            start_point = values_range.lower + floor((values_range.upper - values_range.lower) / 2)

        inner_left_bound = floor(start_point - start_point * 0.05)
        inner_left_bound = inner_left_bound if inner_left_bound in values_range else values_range.lower

        inner_right_bound = ceil(start_point + start_point * 0.05)
        inner_right_bound = inner_right_bound if inner_right_bound in values_range else values_range.upper

        return randint(inner_left_bound, inner_right_bound)

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.counter = self.get_counter()
        self.webinar = self.get_webinar()
        user = self.scope['user']

        if not self.webinar or not user.is_authenticated:
            await self.close(404)
        else:
            if self.counter:
                self.counter.viewers.add(user)

            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            await self.accept()

            for message in ChatMessage.objects.filter(webinar=self.webinar):
                await self.send(text_data=json.dumps({
                    'message': message.text,
                    'username': '{}'.format(message.created_by.username) if message.created_by.username else None,
                    'email': '{}'.format(message.created_by.email),
                    'datetime': message.created.strftime('%Y-%m-%d %H:%M:%S.%f'),
                    'chatType': 'public' if message.webinar else message.webinar.chat_type,
                    'watched': user in message.watched_by.all()
                }))
                message.watched_by.add(user)

            await self.run_receiver()

    async def run_receiver(self):
        pass

    async def disconnect(self, close_code):
        if self.counter and self.scope['user'].is_authenticated:
            self.counter.viewers.remove(self.scope['user'])

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
        user = self.scope['user']

        chat_message = ChatMessage.objects.create(
            webinar=self.webinar,
            text=message,
            created_by=user
        )
        chat_message.watched_by.add(user)

        await self.send(text_data=json.dumps({
            'message': message,
            'username': '{}'.format(user.username) if user.username else None,
            'email': '{}'.format(user.email),
            'datetime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),
            'chatType': 'public' if self.webinar else self.webinar.chat_type
        }))


class GetOnlineConsumer(ChatConsumer):
    async def run_receiver(self):
        await self.get_online({})

    async def get_online(self, event):
        while True:
            if self.counter:
                if self.counter.is_fake:
                    online_count = self.get_fake_count(self.counter.fake_count, self.counter.fake_count_range)
                    self.counter.fake_count = online_count
                    self.counter.save()
                else:
                    online_count = self.counter.viewers.count()
            else:
                online_count = 0

            await self.send(text_data=json.dumps({
                'onlineCount': online_count
            }))

            await asyncio.sleep(10)


class GetChatsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']

        if not user.is_authenticated or not user.is_superuser:
            await self.close(404)
        else:
            webinar_names = Webinar.objects.all().values_list('pk', flat=True)
            chat_name_dict_list = []

            for name in webinar_names:
                latest_message = ChatMessage.objects.filter(webinar__pk=name).latest('created')
                watched = False
                if user in latest_message.watched_by.all():
                    watched = True
                chat_name_dict_list.append({
                    'name': name,
                    'watched': watched
                })

            await self.accept()

            await self.send(text_data=json.dumps(chat_name_dict_list))
