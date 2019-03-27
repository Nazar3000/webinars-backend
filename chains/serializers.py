from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from .models import MessagesChain, Message


# class MessageLinkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MessageLink
#         fields = (
#             'link',
#         )
#
#
# class MessageTextSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MessageText
#         fields = (
#             'text',
#         )
#
#
# class MessageImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MessageImage
#         fields = (
#             'image',
#         )
#
#
# class MessageAudioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MessageAudio
#         fields = (
#             'audio',
#         )
#
#
# class MessageVideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MessageVideo
#         fields = (
#             'video',
#         )
#
#
# class MessageFileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MessageFile
#         fields = (
#             'file',
#         )
#
#
# class MessageDelaySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MessageDelay
#         fields = (
#             'delay',
#         )
#
#
# class MessageButtonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MessageButton
#         fields = (
#             'title',
#             'link',
#             'deactivate_chain_id',
#             'activate_chain_id',
#         )


# class MessageSerializer(WritableNestedModelSerializer):
#     links = MessageLinkSerializer(many=True, allow_null=True)
#     texts = MessageTextSerializer(many=True, allow_null=True, read_only=False)
#     images = MessageImageSerializer(many=True, allow_null=True, read_only=False)
#     audios = MessageAudioSerializer(many=True, allow_null=True, read_only=False)
#     videos = MessageVideoSerializer(many=True, allow_null=True, read_only=False)
#     files = MessageFileSerializer(many=True, allow_null=True, read_only=False)
#     delay = MessageDelaySerializer(allow_null=True, read_only=False)
#     buttons = MessageButtonSerializer(many=True, allow_null=True, read_only=False)
#
#     class Meta:
#         model = Message
#         fields = (
#             'send_datetime',
#             'is_template',
#             'links',
#             'texts',
#             'images',
#             'audios',
#             'videos',
#             'files',
#             'delay',
#             'buttons',
#         )


class MessageSerializer(serializers.ModelSerializer):
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

            'order',
            'delay',
        )


class MessageChainSerializer(WritableNestedModelSerializer):
    messages = MessageSerializer(many=True, required=False)

    class Meta:
        model = MessagesChain
        fields = (
            'title',
            'start_time',
            'is_active',
            'messages'
        )
