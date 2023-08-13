from django.contrib import admin
from facilities_area.models import (
    MasterProfile,
    CustomerProfile,
    Skill,
    MasteryOfSkill,
    Event,
    Task,
)

admin.site.register(MasterProfile)
admin.site.register(CustomerProfile)
admin.site.register(Skill)
admin.site.register(MasteryOfSkill)
admin.site.register(Event)
admin.site.register(Task)
