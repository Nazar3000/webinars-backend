from django.db import models
from projects.models import Project


class BotBase(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    token = models.CharField(max_length=256)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class TelegramBot(BotBase):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Telegram Bot"
        verbose_name_plural = "Telegram Bots"

    def __str__(self):
        return '{} - telegram bot'.format(self.project)


class FacebookBot(BotBase):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Facebook Bot"
        verbose_name_plural = "Facebook Bots"

    def __str__(self):
        return '{} - facebook bot'.format(self.project)