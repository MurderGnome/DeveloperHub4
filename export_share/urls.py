from django.urls import path
from .views import export_project_view, share_project_view

urlpatterns = [
    path('export/<int:project_id>/', export_project_view, name='export_project'),
    path('share/<int:project_id>/', share_project_view, name='share_project'),
]
