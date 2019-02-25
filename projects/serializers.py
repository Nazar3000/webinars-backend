from rest_framework import serializers
from projects.models import Project, Webinar, WebinarFakeChatMessage


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description',)


class UpdateActivationProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('is_active', )


class WebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
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


class WebinarFakeChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebinarFakeChatMessage
        fields = '__all__'


class WebinarFakeMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebinarFakeChatMessage
        exclude = ('name', 'nickname', )
