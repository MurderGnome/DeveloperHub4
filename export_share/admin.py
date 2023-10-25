from django.contrib import admin
from .models import ExportedProject, SharedProject

admin.site.register(ExportedProject)
admin.site.register(SharedProject)