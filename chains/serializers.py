from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


from .models import MessagesChain, Message, MessageLink, MessageAudio, MessageButton, MessageDelay, MessageFile, \
    MessageImage, MessageText, MessageVideo


class MessageChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesChain
        fields = '__all__'


class MessageLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageLink
        fields = '__all__'


class MessageTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageText
        fields = '__all__'


class MessageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageImage
        fields = '__all__'


class MessageAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageAudio
        fields = '__all__'


class MessageVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageVideo
        fields = '__all__'


class MessageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageFile
        fields = '__all__'


class MessageDelaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageDelay
        fields = '__all__'


class MessageButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageButton
        fields = '__all__'


class MessageSerializer(WritableNestedModelSerializer):
    links = MessageLinkSerializer(many=True, allow_null=True)
    texts = MessageTextSerializer(many=True, allow_null=True)
    images = MessageImageSerializer(many=True, allow_null=True)
    audios = MessageAudioSerializer(many=True, allow_null=True)
    videos = MessageVideoSerializer(many=True, allow_null=True)
    files = MessageFileSerializer(many=True, allow_null=True)
    delay = MessageDelaySerializer(allow_null=True)
    buttons = MessageButtonSerializer(many=True, allow_null=True)

    class Meta:
        model = Message
        fields = (
            'pk',
            'send_datetime',
            'chain',
            'links',
            'texts',
            'images',
            'audios',
            'videos',
            'files',
            'delay',
            'buttons',
        )
