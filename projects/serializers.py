from rest_framework import serializers
from projects.models import Project, Webinar, AutoWebinar


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
        # fields = ('project', 'video', 'title', 'description', 'is_active', 'active_chats',
        #           'date_activate', 'user_counter', 'min_fake_user_count', 'image_cover',
        #           'max_fake_user_count', 'cover_type', 'video_cover', )
        fields = '__all__'


class AutoWebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoWebinar
        fields = '__all__'


class UserCountSerializer(serializers.Serializer):
    counter = serializers.IntegerField(min_value=0)
