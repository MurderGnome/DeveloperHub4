from django.db import models
from projects.models import Project

class ExportedProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    export_format = models.CharField(max_length=4, choices=[('PDF', 'PDF')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Export of {self.project.name} as {self.export_format}"

class SharedProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    shared_with_email = models.EmailField()
    shared_link = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shared {self.project.name} with {self.shared_with_email}"