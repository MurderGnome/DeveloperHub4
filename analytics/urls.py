from django.urls import path
from .views import lesson_change_view

urlpatterns = [
    path('changes/<int:project_id>/', lesson_change_view, name='lesson_changes'),
]