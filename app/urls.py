from django.urls import path
from . import views
from django.contrib.auth import logout

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-project/', views.add_project, name='add-project'),
    path('projects/', views.projects, name='projects'),
    path('archived-projects/', views.archived_projects, name='archived-projects'),
    path('single-project/<project_id>', views.single_project, name='single-project'),
    path('archive-project/<project_id>', views.archive_project, name='archive-project'),
    path('remove-attachment/<project_id>/<attachment_id>', views.remove_attachment, name='remove-attachment'),
    path('remove-comment/<project_id>/<comment_id>', views.remove_comment, name='remove-comment'),
]