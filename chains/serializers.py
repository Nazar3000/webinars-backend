from rest_framework import serializers

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


class MessageChainSerializer(serializers.ModelSerializer):
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

        if messages:
            Message.objects.bulk_create([
                Message(**msg)
                for msg in messages
            ])

        chain = MessagesChain.objects.create(**validated_data)
        return chain
