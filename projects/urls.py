from django.urls import path
from .views import new_project_view, project_dashboard_view, dashboard_view

urlpatterns = [
    path('new_project/', new_project_view, name='new_project'),
  
  path('project_dashboard/', project_dashboard_view, name='project_dashboard'),
  
    path('dashboard/', dashboard_view, name='dashboard'),
]
