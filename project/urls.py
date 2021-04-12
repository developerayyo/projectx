from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('project/detail/<int:pk>/', views.detail, name="detail"),
]