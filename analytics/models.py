from django.db import models
from projects.models import Project
from user_profiles.models import UserProfile

class LessonChange(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=255)
    change_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Change in {self.lesson_name} by {self.user.email}"