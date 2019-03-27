from django.contrib.postgres.fields import ArrayField
from django.db import models
from projects.models import Project
from chains.managers import MessageUserTemplateManager, MessageServiceTemplateManager, MessagesManager


class MessagesChain(models.Model):
    title = models.CharField(max_length=256)
    start_time = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Messages Chain"
        verbose_name_plural = "Messages Chains"

    def __str__(self):
        return '{} - {}'.format(self.project, self.title)


class Message(models.Model):
    chain = models.ForeignKey(
        MessagesChain,
        on_delete=models.CASCADE,
        related_name='chains_message',
        blank=True,
        null=True,
    )
    is_template = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField()
    delay = models.PositiveIntegerField(default=0)

    # timer = ''
    text = models.TextField(null=True, blank=True)
    # button = ''
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='messages/images', null=True, blank=True)
    audio = models.FileField(upload_to='messages/audio', null=True, blank=True)
    video = models.FileField(upload_to='messages/videos', null=True, blank=True)
    file = models.FileField(upload_to='messages/files', null=True, blank=True)
    map = ArrayField(
        models.DecimalField(max_digits=11, decimal_places=7),
        size=2,
        blank=True,
        null=True
    )  # [latitude, longitude]

    # msg_type = models.CharField()

    sent_to = models.ManyToManyField('users.CustomUser', blank=True)

    # managers:
    objects = models.Manager()
    messages = MessagesManager()
    user_templates = MessageUserTemplateManager()
    service_templates = MessageServiceTemplateManager()

    class Meta:
        unique_together = ('order', 'chain')

    def __str__(self):
        return '{} - {}'.format(self.chain, self.id)

    def save(self, *args, **kwargs):
        # TODO: make celery task
        super().save(*args, **kwargs)
