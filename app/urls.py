from django.urls import path
from . import views
from django.contrib.auth import logout

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_project/', views.add_project, name='add_project'),
    path('projects/', views.projects, name='projects'),
    path('single_project/<project_id>', views.single_project, name='single_project'),
    path('remove_attachment/<project_id>/<attachment_id>', views.remove_attachment, name='remove_attachment'),
    path('remove_comment/<project_id>/<comment_id>', views.remove_comment, name='remove_comment'),
]