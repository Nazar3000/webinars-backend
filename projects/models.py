from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from users.models import CustomUser

from random import randint
from projects.utils.generator import generate_nickname, generate_name


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated date')

    class Meta:
        abstract = True


class Project(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='User')
    name = models.CharField(max_length=255, verbose_name='Project name')
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    is_active = models.BooleanField(default=True, verbose_name='Is active?')

    def __str__(self):
        return self.name


class Webinar(TimeStampedModel):
    CHATS = (
        ('private', 'private'),
        ('public', 'public'),
    )
    USER_COUNTER_TYPES = (
        ('fake', 'fake'),
        ('real', 'real')
    )

    slug = models.SlugField(max_length=16, primary_key=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    viewers = models.ManyToManyField(CustomUser, blank=True)  # invited viewers
    video = models.FileField(
        upload_to='projects/webinar/video',
        blank=True,
        null=True,
        verbose_name='Webinar video')

    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Title')
    description = models.TextField(max_length=4095, null=True, blank=True, verbose_name='Description')
    is_active = models.BooleanField(default=False, verbose_name='Is active?')

    chat_type = models.CharField(
        choices=CHATS,
        max_length=14,
        blank=True,
        default='public'
    )

    stream_datetime = models.DateTimeField()

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

    video_cover = models.FileField(
        upload_to='projects/webinar/video_cover',
        blank=True,
        null=True,
        verbose_name='Webinar video cover'
    )
    image_cover = models.ImageField(
        upload_to='projects/webinar/image_cover',
        blank=True,
        null=True,
        verbose_name='Webinar image cover'
    )

    def __str__(self):
        return '{} {}'.format(self.slug, self.title)

    @property
    def fake_user_count(self):
        if self.min_fake_user_count and self.max_fake_user_count:
            return randint(self.min_fake_user_count, self.max_fake_user_count)
        else:
            return None

    class Meta:
        verbose_name = 'Webinar'
        verbose_name_plural = 'Webinars'


class WebinarOnlineWatchersCount(models.Model):
    webinar = models.OneToOneField(Webinar, on_delete=models.CASCADE)

    is_fake = models.BooleanField(default=False)
    fake_count = models.PositiveIntegerField(default=0, null=True, blank=True)  # null if not using fake counter
    fake_count_range = IntegerRangeField(null=True, blank=True)

    viewers = models.ManyToManyField(CustomUser, blank=True)  # actual viewers


class FakeChatMessageBase(models.Model):
    name = models.CharField(max_length=63, null=True, blank=True, verbose_name='Fake name')
    nickname = models.CharField(max_length=63, null=True, blank=True, verbose_name='Fake nickname')
    message = models.TextField(max_length=4095, null=True, blank=True)
    display_time = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.name = generate_name(locale_list=['en', 'uk_UA'])
        self.nickname = generate_nickname()
        super(FakeChatMessageBase, self).save(*args, **kwargs)


class WebinarFakeChatMessage(FakeChatMessageBase):
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE, verbose_name='Webinar')
    name = models.CharField(max_length=63, null=True, blank=True, verbose_name='Fake name')
    nickname = models.CharField(max_length=63, null=True, blank=True, verbose_name='Fake nickname')
    message = models.TextField(max_length=4095, null=True, blank=True)
    display_time = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')

    class Meta:
        verbose_name = 'Fake webinar message'
        verbose_name_plural = 'Fake webinar messages'

    def save(self, *args, **kwargs):
        self.name = generate_name(locale_list=['en', 'uk_UA'])
        self.nickname = generate_nickname()
        super(FakeChatMessageBase, self).save(*args, **kwargs)
