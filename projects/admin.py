from django.contrib import admin
from projects.models import Project, Webinar, WebinarFakeChatMessage


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'description', 'created', 'updated', 'is_active')
    readonly_fields = ('created', 'updated')
    list_display_links = ('id', 'name')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Webinar)
admin.site.register(WebinarFakeChatMessage)
