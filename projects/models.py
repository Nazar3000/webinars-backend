from django.db import models
from users.models import CustomUser

from random import randint
from multiselectfield import MultiSelectField
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
    COVER_TYPES = (
        ('video', 'video'),
        ('image', 'image'),
    )

    slug = models.SlugField(max_length=16, primary_key=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    viewers = models.ManyToManyField(CustomUser, null=True, blank=True)
    video = models.FileField(
        upload_to='projects/webinar/video/',
        blank=True,
        null=True,
        verbose_name='Webinar video')

    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Title')
    description = models.TextField(max_length=4095, null=True, blank=True, verbose_name='Description')
    is_active = models.BooleanField(default=False, verbose_name='Is active?')

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
    cover_time = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Cover time before video starts (in seconds)')

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
