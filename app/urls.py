from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_project/', views.add_project, name='add_project'),
    path('projects/', views.projects, name='projects'),
    path('single_project/<project_id>', views.single_project, name='single_project'),
    path('update_project/<project_id>', views.update_project, name='update_project'),
]