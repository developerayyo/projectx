from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projects =  Project.objects.all()
    context = {"projects": projects}
    return render(request, 'project/home.html', context)

def detail(request, pk):
    projects = Project.objects.get(pk=pk)
    context = {"projects": projects}
    return render(request, 'project/detail.html', context)