from django.db import models


class Project(models.Model):
    pass


class WebinarBase(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Title')
    description = models.TextField(max_length=4095, null=True, blank=True, verbose_name='Description')

    class Meta:
        abstract = True

    def __str__(self):
        return '{}'.format(self.title)


class Webinar(WebinarBase):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


class AutoWebinar(WebinarBase):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

