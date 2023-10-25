from django.shortcuts import render, redirect
from .models import Project, Dashboard

def new_project_view(request):
    # Handle the logic for creating a new project here
    pass

def project_dashboard_view(request):
    # Display all ongoing and completed projects here
    pass

from django.shortcuts import render, redirect
from .forms import ProjectForm

def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project_dashboard')
    else:
        form = ProjectForm()
    return render(request, 'projects/html/create_project.html', {'form': form})

def project_dashboard(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'projects/html/project_dashboard.html', {'projects': projects})
