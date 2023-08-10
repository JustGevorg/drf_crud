from django.db import models
from common.models import BaseModel
from choices import EducationChoices


class Master(BaseModel):
    education = models.CharField(
        verbose_name="Образование",
        choices=EducationChoices.choices,
        default=None,
        null=True,
        blank=True,
    )
    skills = models.ManyToManyField(
        verbose_name="Умения",
        to="Skill",
        through="MasteryOfSkill",
        unique=True,
        related_name="master_profiles",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "master"
        verbose_name = "Мастера"
        verbose_name_plural = "Мастера"


class CustomerProfile(BaseModel):
    ...

    class Meta:
        db_table = "customer_profile"
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"


class Skill(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=125, unique=True)

    class Meta:
        db_table = "skill"
        verbose_name = "Навык"
        verbose_name_plural = "Навык"


class MasteryOfSkill(BaseModel):
    class Meta:
        db_table = "mastery_of_skill"
        verbose_name = "Владение навыком"
        verbose_name_plural = "Владение навыками"


class Event(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=125)
    duration = models.DurationField(
        verbose_name="Продолжительность",
    )
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    class Meta:
        db_table = "event"
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class Task(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=125)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    reward = models.DecimalField(verbose_name="Вознаграждение")
    event = models.ForeignKey(
        verbose_name="Мероприятие", null=True, blank=True, related_name="tasks"
    )

    class Meta:
        db_table = "task"
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
