from django.db import models
from projects.models import Project


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
    send_datetime = models.DateTimeField(
        verbose_name='Send time'
    )
    chain = models.ForeignKey(MessagesChain, on_delete=models.CASCADE, related_name='chains_message')

    class Meta:
        verbose_name = "Bot Message"
        verbose_name_plural = "Bot Messages"

    def __str__(self):
        return '{} - {}'.format(self.chain, self.id)


class MessageLink(models.Model):
    message = models.ForeignKey(
        Message, 
        on_delete=models.CASCADE,
        related_name='links'
    )
    link = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Message link'
        verbose_name_plural = 'Message links'
    
    def __str__(self):
        return '{}'.format(self.link)


class MessageText(models.Model):
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='texts'
    )
    text = models.TextField(max_length=4096)

    class Meta:
        verbose_name = 'Message text'
        verbose_name_plural = 'Message texts'

    def __str__(self):
        return '{}'.format(self.text)


class MessageImage(models.Model):
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='messages/images')

    class Meta:
        verbose_name = 'Message text'
        verbose_name_plural = 'Message texts'

    def __str__(self):
        return '{}'.format(self.image)


class MessageAudio(models.Model):
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='audios'
    )
    audio = models.FileField(upload_to='messages/audio')

    class Meta:
        verbose_name = 'Message audio'
        verbose_name_plural = 'Message audios'

    def __str__(self):
        return '{}'.format(self.audio)


class MessageVideo(models.Model):
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='videos'
    )
    video = models.FileField(upload_to='messages/videos')

    class Meta:
        verbose_name = 'Message video'
        verbose_name_plural = 'Message videos'

    def __str__(self):
        return '{}'.format(self.video)


class MessageFile(models.Model):
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='files'
    )
    file = models.FileField(upload_to='messages/files')

    class Meta:
        verbose_name = 'Message file'
        verbose_name_plural = 'Message files'

    def __str__(self):
        return '{}'.format(self.file)


class MessageDelay(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name='delay'
    )
    delay = models.IntegerField(
        verbose_name='Delay time (sec)'
    )

    class Meta:
        verbose_name = 'Message delay'
        verbose_name_plural = 'Message delays'

    def __str__(self):
        return '{}'.format(self.delay)


class MessageButton(models.Model):
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='buttons'
    )
    title = models.CharField(
        max_length=256,
        verbose_name='Button title'
    )

    link = models.URLField(
        blank=True, null=True,
        verbose_name='Button link'
    )

    deactivate_chain_id = models.PositiveIntegerField(
        verbose_name='Deactivate chain ID',
        blank=True, null=True,
    )

    activate_chain_id = models.PositiveIntegerField(
        verbose_name='Activate chain ID',
        blank=True, null=True,
    )

    # TODO: add some other action for button

    class Meta:
        verbose_name = 'Message button'
        verbose_name_plural = 'Message buttons'

    def __str__(self):
        return '{}'.format(self.title)



