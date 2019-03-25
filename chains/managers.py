from django.db import models


class MessageUserTemplateManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_template=True, chain__isnull=False)


class MessageServiceTemplateManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_template=True, chain__isnull=True)


class MessagesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_template=True, chain__isnull=False)
