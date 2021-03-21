from django.contrib import admin
from .models import Faculty, Department, Project, User

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(User)
