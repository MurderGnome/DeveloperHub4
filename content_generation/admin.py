from django.contrib import admin
from .models import LearningOutcome, LessonPlan, PlanOfInstruction, Assessment, Rubric, StudentActivity

admin.site.register(LearningOutcome)
admin.site.register(LessonPlan)
admin.site.register(PlanOfInstruction)
admin.site.register(Assessment)
admin.site.register(Rubric)
admin.site.register(StudentActivity)
