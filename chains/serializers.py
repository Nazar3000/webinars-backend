from rest_framework import serializers

from chains.constants import MessageTypes
from .models import MessagesChain, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            # 'timer',
            'text',
            # 'button',
            'link',
            # 'image',
            # 'audio',
            # 'video',
            # 'file',
            'map',

            'msg_type',

            'order',
            'delay',
        )


class MessageFullUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            # 'timer',
            'text',
            # 'button',
            'link',
            'image',
            'audio',
            'video',
            'file',
            'map',

            'msg_type',

            'order',
            'delay',
        )
        extra_kwargs = {
            'msg_type': {'required': False},
            'order': {'required': False},
            'delay': {'required': False},
        }


class MessageFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            # 'timer',
            'text',
            # 'button',
            'link',
            'image',
            'audio',
            'video',
            'file',
            'map',

            'msg_type',

            'order',
            'delay',
        )


class MessageChainCreateSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, required=False)

    class Meta:
        model = MessagesChain
        fields = (
            'id',
            'title',
            'start_time',
            'is_active',
            'messages'
        )

    def create(self, validated_data):
        messages = validated_data.pop('messages', None)

        chain = MessagesChain.objects.create(**validated_data)

        if messages:
            Message.objects.bulk_create([
                Message(chain=chain, **msg)
                for msg in messages
            ])

        return chain


class MessageChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesChain
        fields = (
            'id',
            'title',
            'start_time',
            'is_active',
        )
