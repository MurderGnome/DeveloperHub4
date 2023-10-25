from django.db import models
from projects.models import Project

class MLModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    trained_on = models.DateField()
    accuracy = models.DecimalField(max_digits=5, decimal_places=2)  # store accuracy as a percentage

    def __str__(self):
        return self.name

class PredictedContent(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    ml_model = models.ForeignKey(MLModel, on_delete=models.CASCADE)
    generated_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Generated content for {self.project.name} using {self.ml_model.name}"