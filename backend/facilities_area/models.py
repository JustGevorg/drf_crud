from django.db import models
from common.models import BasePeopleModel, BaseModel
from facilities_area.choices import EducationChoices, CustomerStatusChoices


class MasterProfile(BasePeopleModel):
    education = models.CharField(
        verbose_name="Образование",
        choices=EducationChoices.choices,
        default=None,
        null=True,
        blank=True,
        max_length=125,
    )
    skills = models.ManyToManyField(
        verbose_name="Умения",
        to="Skill",
        through="MasteryOfSkill",
        related_name="master_profiles",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "master"
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CustomerProfile(BasePeopleModel):
    status = models.CharField(
        verbose_name="Статус",
        choices=CustomerStatusChoices.choices,
        default=CustomerStatusChoices.NEWBIE,
        null=True,
        blank=True,
        max_length=64,
    )

    class Meta:
        db_table = "customer_profile"
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Skill(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=125, unique=True)

    class Meta:
        db_table = "skill"
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return f"{self.title}"


class MasteryOfSkill(BaseModel):
    years_experience = models.PositiveSmallIntegerField(
        verbose_name="Опыт (годы)", default=0
    )
    skill = models.ForeignKey(verbose_name="Умение", to=Skill, on_delete=models.CASCADE)
    master = models.ForeignKey(
        verbose_name="Мастер", to=MasterProfile, on_delete=models.CASCADE
    )

    class Meta:
        unique_together = "skill", "master"
        db_table = "mastery_of_skill"
        verbose_name = "Владение навыком"
        verbose_name_plural = "Владение навыками"

    def __str__(self):
        return f"{self.pk}"


class Event(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=125)
    duration = models.IntegerField(
        verbose_name="Продолжительность (дней)",
    )
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    class Meta:
        db_table = "event"
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return f"{self.title}"


class Task(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=125)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    reward = models.DecimalField(
        verbose_name="Вознаграждение", decimal_places=2, max_digits=6
    )
    event = models.ForeignKey(
        to=Event,
        on_delete=models.CASCADE,
        verbose_name="Мероприятие",
        null=True,
        blank=True,
        related_name="tasks",
    )

    class Meta:
        db_table = "task"
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

    def __str__(self):
        return f"{self.title}"
