from django.db import models
from user_profiles.models import UserProfile

class Project(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Dashboard(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return f"{self.user.username}'s Dashboard"
