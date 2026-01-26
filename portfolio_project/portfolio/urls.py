from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('experience/', views.experience_list, name='experience'),
    path('projects/', views.projects_list, name='projects'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('contact/ajax/', views.contact_ajax, name='contact_ajax'),
    path('download-resume/', views.download_resume, name='download_resume'),
]