from django.contrib import admin
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'description', 'created', 'updated', 'is_active', 'cover_time')
    readonly_fields = ('created', 'updated')
    list_display_links = ('id', 'name')


admin.site.register(Project, ProjectAdmin)


