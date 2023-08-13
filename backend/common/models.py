from django.utils import timezone
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name="Создано", db_index=True, default=timezone.now()
    )
    updated_at = models.DateTimeField(verbose_name="Обновлено", auto_now=True)

    class Meta:
        abstract = True


class BasePeopleModel(BaseModel):
    first_name = models.CharField(verbose_name="Имя", max_length=64)
    last_name = models.CharField(verbose_name="Фмилия", max_length=64)
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")

    class Meta:
        abstract = True
