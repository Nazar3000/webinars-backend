from django.db import models


class MessageUserTemplateManager(models.Manager):

    def get_queryset(self):
        return super(MessageUserTemplateManager, self).get_queryset().filter(is_template=True, chain__isnull=False)


class MessageServiceTemplateManager(models.Manager):

    def get_queryset(self):
        return super(MessageServiceTemplateManager, self).get_queryset().filter(is_template=True, chain__isnull=True)


class MessagesManager(models.Manager):

    def get_queryset(self):
        return super(MessagesManager, self).get_queryset().filter(is_template=True, chain__isnull=False)
