from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True


class Media(BaseModel):
    file_url = models.URLField(_("file URL"), max_length=500)

    class Meta:
        verbose_name = _("media")
        verbose_name_plural = _("media")

    def __str__(self):
        return self.file_url


class Education(BaseModel):
    name = models.CharField(_("name"), max_length=100)

    class Meta:
        verbose_name = _("education")
        verbose_name_plural = _("educations")

    def __str__(self):
        return self.name
