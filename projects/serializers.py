from rest_framework import serializers
from projects.models import Project, Webinar, AutoWebinar, WebinarFakeChatMessage, AutoWebinarFakeChatMessage


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'user', 'name', 'description', 'is_active', 'cover_time')


class UpdateActivationProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('is_active', )


class WebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = '__all__'


class AutoWebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoWebinar
        fields = '__all__'


class UserCountSerializer(serializers.Serializer):
    counter = serializers.IntegerField(min_value=0)


class WebinarChatActivateBase(serializers.ModelSerializer):
    CHATS = (
        ('private', 'private'),
        ('public', 'public'),
    )

    active_chats = serializers.MultipleChoiceField(choices=CHATS)

    class Meta:
        abstract = True


class WebinarChatActivateSerializer(WebinarChatActivateBase):
    class Meta:
        model = Webinar
        fields = ('active_chats', )


class AutoWebinarChatActivateSerializer(WebinarChatActivateBase):
    class Meta:
        model = AutoWebinar
        fields = ('active_chats', )


class WebinarFakeChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebinarFakeChatMessage
        fields = '__all__'


class WebinarFakeMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebinarFakeChatMessage
        exclude = ('name', 'nickname', )


class AutoWebinarFakeMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoWebinarFakeChatMessage
        exclude = ('name', 'nickname', )


class AutoWebinarFakeChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoWebinarFakeChatMessage
        fields = '__all__'

