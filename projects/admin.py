from django.contrib import admin
from projects.models import Project, Webinar, WebinarFakeChatMessage, WebinarOnlineWatchersCount


class WebinarOnlineWatchersCountInline(admin.TabularInline):
    model = WebinarOnlineWatchersCount


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'description', 'created', 'updated', 'is_active')
    readonly_fields = ('created', 'updated')
    list_display_links = ('id', 'name')


class WebinarAdmin(admin.ModelAdmin):
    fields = (
        'slug',
        'project',
        'viewers',
        'video',
        'title',
        'description',
        'is_active',
        'active_chats',
        'stream_datetime',
        'user_counter',
        'min_fake_user_count',
        'max_fake_user_count',
        'video_cover',
        'image_cover',
        'cover_time',
    )
    inlines = (WebinarOnlineWatchersCountInline,)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Webinar, WebinarAdmin)
admin.site.register(WebinarFakeChatMessage)
