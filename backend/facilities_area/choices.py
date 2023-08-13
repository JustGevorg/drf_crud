from django.db.models import TextChoices


class EducationChoices(TextChoices):
    SELF_TAUGHT = "ST", "Самоучка"
    TRAINING_COURSES = "TC", "Курсы подготовки"
    SPECIAL_EDUCATION = "SE", "Среднее специальное"
    HIGHER_EDUCATION = "HE", "Высшее"


class CustomerStatusChoices(TextChoices):
    NEWBIE = "N", "Новый заказчик"
    ORDINARY = "O", "Обычный заказчик"
    REGULAR = "R", "Постоянный заказчик"
