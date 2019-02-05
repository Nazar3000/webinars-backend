from django.db import models
from projects.models import Project


class TelegramBot(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    token = models.CharField(max_length=256)
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Telegram Bot"
        verbose_name_plural = "Telegram Bots"

    def __str__(self):
        return '{}'.format(self.project)


