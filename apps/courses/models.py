from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from apps.common.models import BaseModel
from apps.courses.choices import LessonTypeChoices
from apps.payments.choices import CurrencyEnum
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.courses.managers import UserManager
from django.core.validators import RegexValidator
from apps.courses.choicess import GenderChoices


class Category(BaseModel):
    name = models.CharField(_("name"), max_length=255)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(_("name"), max_length=255)

    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")

    def __str__(self):
        return self.name


class Course(BaseModel):
    author = models.ForeignKey(
        "accounts.Author",
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name=_("author"),
    )
    banner = models.ForeignKey(
        "common.Media",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="course_banners",
        verbose_name=_("banner"),
    )
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"), blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses",
        verbose_name=_("category"),
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="courses",
        verbose_name=_("tags"),
    )
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(
        _("currency"),
        max_length=20,
        choices=CurrencyEnum.choices,
        default=CurrencyEnum.UZS,
    )
    reward_stars = models.PositiveIntegerField(_("reward stars"), default=0)
    is_active = models.BooleanField(_("is active"), default=True)
    is_published = models.BooleanField(_("is published"), default=False)

    class Meta:
        verbose_name = _("course")
        verbose_name_plural = _("courses")

    def __str__(self):
        return self.name


class Module(BaseModel):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="modules",
        verbose_name=_("course"),
    )
    name = models.CharField(_("name"), max_length=255)
    course_order = models.PositiveIntegerField(_("course order"), default=0)

    class Meta:
        verbose_name = _("module")
        verbose_name_plural = _("modules")
        ordering = ["course_order"]

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name="lessons",
        verbose_name=_("module"),
    )
    video = models.ForeignKey(
        "common.Media",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="lesson_videos",
        verbose_name=_("video"),
    )
    online_url = models.URLField(
        _("Online URL (YouTube, Vimeo, etc.)"), max_length=500, blank=True
    )
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"), blank=True)
    current_rating = models.FloatField(_("current rating"), default=0)
    type = models.CharField(_("type"), max_length=50, choices=LessonTypeChoices.choices)
    max_attempts_count = models.PositiveIntegerField(_("max attempts count"), default=0)
    attempt_interval = models.PositiveIntegerField(_("attempt interval"), default=0)
    lesson_order = models.PositiveIntegerField(_("lesson order"), default=0)
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        verbose_name = _("lesson")
        verbose_name_plural = _("lessons")
        ordering = ["lesson_order"]

    def __str__(self):
        return self.name


class Enrollment(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="enrollments",
        verbose_name=_("user"),
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="enrollments",
        verbose_name=_("course"),
    )
    started_at = models.DateTimeField(_("started at"), auto_now_add=True)
    finished_at = models.DateTimeField(_("finished at"), null=True, blank=True)

    class Meta:
        verbose_name = _("enrollment")
        verbose_name_plural = _("enrollments")
        unique_together = ("user", "course")

    def __str__(self):
        return f"{self.user} - {self.course}"


class LessonEnrollment(BaseModel):
    lesson = models.ForeignKey(
        # "courses.Lesson",
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="lessons",
        verbose_name=_("lesson"),
    )
    stars_count = models.IntegerField(default=0)
    process = models.CharField(max_length=100)

    class Meta:
        verbose_name = "lessonenrollment"
        verbose_name_plural = "lessonsenrollments"

    def __str__(self):
        return f"{self.lesson} - {self.enrollment}"