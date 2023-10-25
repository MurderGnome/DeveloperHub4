from django.urls import path
from .views import new_project_view, project_dashboard_view

urlpatterns = [
    path('new_project/', new_project_view, name='new_project'),
    path('dashboard/', project_dashboard_view, name='project_dashboard'),
]
