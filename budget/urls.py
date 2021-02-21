from django.urls import path
from django.contrib import admin
from . import views

"""The url's listed below are url's that the user can get redirected to"""
urlpatterns = [
    path('list/', views.project_list, name='list'),
    path('', views.home, name="home"),
    path('add/', views.ProjectCreateView.as_view(), name='add'),
    path('add/<slug:project_slug>', views.project_detail, name='detail'),
]