from django.db import models

from bots.constants import BotTypes


class BotBase(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    api_key = models.CharField(max_length=256)
    active = models.BooleanField(default=True)
    user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE)
    bot_type = models.CharField(max_length=8, choices=BotTypes.BOT_TYPES)

    def __str__(self):
        return self.bot_type
