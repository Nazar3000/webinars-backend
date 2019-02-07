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


class ViberBot(BotBase):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Viber Bot"
        verbose_name_plural = "Viber Bots"


class WhatsAppBot(BotBase):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "WhatsApp Bot"
        verbose_name_plural = "WhatsApp Bots"


class MessagesChain(models.Model):
    title = models.CharField(max_length=256)
    start_time = models.DateTimeField()
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Messages Chain"
        verbose_name_plural = "Messages Chains"

    def __str__(self):
        return '{} - {}'.format(self.project, self.title)


class BotMessage(models.Model):
    text = models.TextField()
    interval = models.PositiveIntegerField(verbose_name='interval (hours)')
    chain = models.ForeignKey(MessagesChain, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Bot Message"
        verbose_name_plural = "Bot Messages"

    def __str__(self):
        return '{} - {}'.format(self.chain, self.id)
