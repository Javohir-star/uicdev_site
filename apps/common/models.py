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


class Country(BaseModel):
    name = models.CharField(_("name"), max_length=100)

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")

    def __str__(self):
        return self.name


class Region(BaseModel):
    name = models.CharField(_("name"), max_length=100)

    class Meta:
        verbose_name = _("region")
        verbose_name_plural = _("regions")

    def __str__(self):
        return self.name


class Education(BaseModel):
    name = models.CharField(_("name"), max_length=100)

    class Meta:
        verbose_name = _("education")
        verbose_name_plural = _("educations")

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
        return self.first_name, self.last_name, self.age, self.gender


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


class Course(BaseModel):
    name = models.CharField(_("name"), max_length=100)
    start_date = models.DateField(_("start date"))
    end_date = models.DateField(_("end date"))
    teacher = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="courses")

    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")

    def __str__(self):
        return self.name
