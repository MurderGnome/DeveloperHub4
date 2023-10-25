from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    # Extend the user model here, e.g.,
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    history = models.JSONField(default=dict)  # to store project history
    
    def __str__(self):
        return self.username