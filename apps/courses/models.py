from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.courses.models import Author, BaseModel


class Category(BaseModel):
    name = models.CharField(_("name"), max_length=100)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(_("name"), max_length=100)

    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")

    def __str__(self):
        return self.name


class Author(BaseModel):
    full_name = models.CharField(_("full name"), max_length=100)
    age = models.IntegerField(_("age"), default=None)
    gender = models.CharField(_("gender"), max_length=100)

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")

    def __str__(self):
        return self.full_name, self.age, self.gender
