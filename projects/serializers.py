from drf_extra_fields.fields import Base64ImageField, Base64FileField
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
    cover_image = Base64ImageField(source='image_cover', required=False)
    cover_video = Base64FileField(source='video_cover', required=False)

    class Meta:
        model = Webinar
        fields = (
            'slug',
            'video',
            'title',
            'description',
            'stream_datetime',
            'cover_video',
            'cover_image',
            'cover_time',
            'chat_type'
        )


class UserCountSerializer(serializers.Serializer):
    counter = serializers.IntegerField(min_value=0)


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
