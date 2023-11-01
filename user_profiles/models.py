from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserProfile(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    history = models.JSONField(default=dict)

    # Define custom related names for groups and user_permissions to avoid reverse accessor clashes
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name="custom_user_groups",
        verbose_name=_('groups')
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name="custom_user_permissions",
        verbose_name=_('user permissions')
    )

    def __str__(self):
        return self.username
