from django.contrib import admin
from .models import MessagesChain, Message, MessageDelay, MessageVideo, MessageText, MessageImage, MessageFile, \
    MessageButton, MessageAudio, MessageLink

admin.site.register(MessagesChain)


class MessageLinkTabularInline(admin.TabularInline):
    model = MessageLink
    fields = (
        'message',
        'link',
    )
    extra = 0


class MessageTextTabularInline(admin.TabularInline):
    model = MessageText
    fields = (
        'message',
        'text',
    )
    extra = 0


class MessageImageTabularInline(admin.TabularInline):
    model = MessageImage
    fields = (
        'message',
        'image',
    )
    extra = 0


class MessageAudioTabularInline(admin.TabularInline):
    model = MessageAudio
    fields = (
        'message',
        'audio',
    )
    extra = 0


class MessageVideoTabularIline(admin.TabularInline):
    model = MessageVideo
    fields = (
        'message',
        'video',
    )
    extra = 0


class MessageFileTabularInline(admin.TabularInline):
    model = MessageFile
    fields = (
        'message',
        'file',
    )
    extra = 0


class MessageDelayTabularInline(admin.TabularInline):
    model = MessageDelay
    fields = (
        'message',
        'delay',
    )
    extra = 1
    max_num = 1


class MessageButtonTabularInline(admin.TabularInline):
    model = MessageButton
    fields = (
        'message',
        'title',
        'link',
        'deactivate_chain_id',
        'activate_chain_id'
    )
    extra = 0


class MessageAdmin(admin.ModelAdmin):

    inlines = (
        MessageLinkTabularInline,
        MessageTextTabularInline,
        MessageImageTabularInline,
        MessageAudioTabularInline,
        MessageVideoTabularIline,
        MessageFileTabularInline,
        MessageDelayTabularInline,
        MessageButtonTabularInline,
    )
    fields = (
        'send_datetime',
        'chain',
    )


admin.site.register(Message, MessageAdmin)
