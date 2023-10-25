from django.urls import path
from .views import generate_content_view

urlpatterns = [
    path('generate/<int:project_id>/', generate_content_view, name='generate_content'),
]