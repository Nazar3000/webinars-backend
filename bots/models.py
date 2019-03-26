from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from bots.constants import BotTypes
from chains.models import MessagesChain
from projects.models import Webinar
from chains.helpers import start_bot_chain, bot_init


class BotBase(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    api_key = models.CharField(max_length=256)
    active = models.BooleanField(default=True)
    user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE)
    bot_type = models.CharField(max_length=8, choices=BotTypes.BOT_TYPES)

    telegram_chat_id = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.bot_type

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.active and not self.telegram_chat_id:
            bot_init(self.api_key, self.pk)


@receiver(post_save, sender=BotBase)
def send_bot_chain_messages(sender, instance, created, **kwargs):
    project_pks = Webinar.objects.filter(viewers__pk__exact=instance.user.pk)\
        .values_list('project', flat=True)
    chains = MessagesChain.objects.filter(project__pk__in=project_pks)

    for chain in chains:
        if instance.telegram_chat_id:
            start_bot_chain(chain, instance)
