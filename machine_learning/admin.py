from django.contrib import admin
from .models import MLModel, PredictedContent

admin.site.register(MLModel)
admin.site.register(PredictedContent)