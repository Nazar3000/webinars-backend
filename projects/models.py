from django.db import models


class Project(models.Moel):
    pass


class WebinarBase(models.Model):
    class Meta:
        abstract = True


class Webinar(WebinarBase):
    pass


class AutoWebinar(WebinarBase):
    pass
