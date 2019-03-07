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
    links = MessageLinkSerializer(many=True)
    texts = MessageTextSerializer(many=True)
    images = MessageImageSerializer(many=True)
    audios = MessageAudioSerializer(many=True)
    videos = MessageVideoSerializer(many=True)
    files = MessageFileSerializer(many=True)
    delay = MessageDelaySerializer()
    buttons = MessageButtonSerializer


    class Meta:
        model = Message
        fields = '__all__'