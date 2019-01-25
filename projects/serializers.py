from rest_framework import serializers
from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('user', 'name', 'description', 'is_active', 'cover_time')


class UpdateActivationProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('is_active', )
