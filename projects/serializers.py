from rest_framework import serializers
from projects.models import Project, Webinar, WebinarFakeChatMessage


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'is_active',)

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs.keys():
            self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        validated_data['user'] = self.user
        return super().create(validated_data)


class WebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = (
            'slug',
            'video',
            'title',
            'description',
            'stream_datetime',
            'video_cover',
            'image_cover',
            'cover_time',
        )


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


class WebinarPermissionSerializer(serializers.Serializer):
    slug = serializers.SlugField(max_length=16)
    user_id = serializers.IntegerField()
