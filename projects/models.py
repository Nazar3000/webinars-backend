from django.db import models
from users.models import CustomUser

from random import randint
from multiselectfield import MultiSelectField
from projects.utils.generator import generate_nickname, generate_name


class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='User')
    name = models.CharField(max_length=255, verbose_name='Project name')
    description = models.TextField(max_length=4095, null=True, blank=True, verbose_name='Description')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated date')

    is_active = models.BooleanField(default=True, verbose_name='Is active?')
    cover_time = models.PositiveIntegerField(null=True, blank=True,
                                             verbose_name='Cover time before video starts (in seconds)')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return '{}'.format(self.name)

    def __unicode__(self):
        return self.name


class WebinarBase(models.Model):
    CHATS = (
        ('private', 'private'),
        ('public', 'public'),
    )
    USER_COUNTER_TYPES = (
        ('fake', 'fake'),
        ('real', 'real')
    )
    COVER_TYPES = (
        ('video', 'video'),
        ('image', 'image'),
    )

    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Title')
    description = models.TextField(max_length=4095, null=True, blank=True, verbose_name='Description')
    is_active = models.BooleanField(default=False, verbose_name='Is active?')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated date')

    active_chats = MultiSelectField(
        choices=CHATS,
        max_choices=2,
        max_length=14,
        null=True,
        blank=True,
        verbose_name='Active chats'
    )

    # TODO: 'date_activate' must be rewritten:
    date_activate = models.DateTimeField(null=True, blank=True, verbose_name="Activate date")

    user_counter = models.CharField(
        choices=USER_COUNTER_TYPES,
        max_length=4,
        null=True,
        blank=True,
        verbose_name='User counter type'
    )
    min_fake_user_count = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name='Minimum value for fake people count'
    )
    max_fake_user_count = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name='Maximum value for fake people count'
    )
    cover_type = models.CharField(
        max_length=5,
        choices=COVER_TYPES,
        null=True,
        blank=True,
        verbose_name="Cover before video"
    )
    video_cover = models.FileField(
        upload_to='projects/webinar/video_cover/',
        blank=True,
        null=True,
        verbose_name='Webinar video cover'
    )
    image_cover = models.ImageField(
        upload_to='projects/webinar/image_cover/',
        blank=True,
        null=True,
        verbose_name='Webinar image cover'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return '{}'.format(self.title)

    def __unicode__(self):
        return self.title

    @property
    def fake_user_count(self):
        if self.min_fake_user_count and self.max_fake_user_count:
            return randint(self.min_fake_user_count, self.max_fake_user_count)
        else:
            return None


class AutoWebinar(WebinarBase):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    # TODO: Write the url or smth else which associated with streaming video.

    class Meta:
        verbose_name = 'Auto Webinar'
        verbose_name_plural = 'Auto Webinars'


class Webinar(WebinarBase):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    video = models.FileField(
        upload_to='projects/webinar/video/',
        blank=True,
        null=True,
        verbose_name='Webinar video')

    class Meta:
        verbose_name = 'Webinar'
        verbose_name_plural = 'Webinars'


class FakeChatMessageBase(models.Model):
    name = models.CharField(max_length=63, null=True, blank=True, verbose_name='Fake name')
    nickname = models.CharField(max_length=63, null=True, blank=True, verbose_name='Fake nickname')
    message = models.TextField(max_length=4095, null=True, blank=True)
    display_time = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.name = generate_name(locale_list=['en', 'uk_UA'])
        self.nickname = generate_nickname()
        super(FakeChatMessageBase, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class WebinarFakeChatMessage(FakeChatMessageBase):
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE, verbose_name='Webinar')

    class Meta:
        verbose_name = 'Fake webinar message'
        verbose_name_plural = 'Fake webinar messages '


class AutoWebinarFakeChatMessage(FakeChatMessageBase):
    auto_webinar = models.ForeignKey(AutoWebinar, on_delete=models.CASCADE, verbose_name='Auto webinar')

    class Meta:
        verbose_name = 'Fake autowebinar message'
        verbose_name_plural = 'Fake autowebinar messages'
