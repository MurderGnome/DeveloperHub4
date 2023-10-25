
from django.db import models
from user_profiles.models import UserProfile

class Course(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    course_development_manager_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.module_name

class STSLineItem(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    sts_item_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sts_item_name

class LearningOutcome(models.Model):
    sts_line_item = models.ForeignKey(STSLineItem, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class STSLineItem(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='sts_line_items')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class LearningOutcome(models.Model):
    sts_line_item = models.ForeignKey(STSLineItem, on_delete=models.CASCADE, related_name='learning_outcomes')
    name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name
