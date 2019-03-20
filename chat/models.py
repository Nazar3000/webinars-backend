from django.db import models

from projects.models import TimeStampedModel


class ChatMessage(TimeStampedModel):
    webinar = models.ForeignKey('projects.Webinar', on_delete=models.CASCADE)
    watched_by = models.ManyToManyField('users.CustomUser', blank=True)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='created_chat_messages')
    text = models.TextField()

    def __str__(self):
        return self.webinar.slug
