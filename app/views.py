from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime
from .forms import AttachmentForm, ProjectForm, CommentForm
from .models import Project, Attachment, Comment
import os
from django.conf import settings

def index(request):
    context = {'year':datetime.datetime.now().year}
    return render(request, 'app/index.html', context)

def login_view(request):
    context = {'year':datetime.datetime.now().year}
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('app:dashboard')
        else:
            return render(request, 'app/index.html', context)    
    else:
        return render(request, 'app/index.html', context)

def logout_view(request):
    return redirect('app:index')

def dashboard(request):
    projects = Project.objects.all()
    archived_projects_count = Project.objects.filter(archived=True).count()
    usersCount = User.objects.all().count()
    attachmentsCount = Attachment.objects.all().count()

    context = {'year':datetime.datetime.now().year,
               'projects':projects,
               'archived_projects_count':archived_projects_count,
               'usersCount':usersCount,
               'attachmentsCount':attachmentsCount
               }

    return render(request, 'app/dashboard.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {'year':datetime.datetime.now().year,
               'projects':projects}
    return render(request, 'app/projects.html', context)

def archived_projects(request):
    projects = Project.objects.filter(archived=True)
    context = {'year':datetime.datetime.now().year,
               'projects':projects}
    return render(request, 'app/archived-projects.html', context)

def add_project(request):
    if request.method == 'POST':
        f = ProjectForm(data=request.POST)
        
        if f.is_valid():
            p = f.save()

            prj = Project.objects.filter(name=p.name)
            
            files = request.FILES.getlist('file')
            for fl in files:
                att = Attachment(name=str(fl), file=fl, project_id=prj[0].id)
                att.save()
                
            return redirect('app:add-project')
    else:
        form_at = AttachmentForm()
        form = ProjectForm()
        context = {'year':datetime.datetime.now().year,
                   'form_at':form_at,
                   'form':form}

        return render(request, 'app/add-project.html', context)

def single_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    attachments = Attachment.objects.filter(project_id=project_id)
    comments = Comment.objects.filter(project_id=project_id).order_by('-id')

    form = ProjectForm(instance=project)
    form_at = AttachmentForm()
    form_com = CommentForm()

    context = {'project' : project,
               'form':form,
               'form_at':form_at,
               'form_com':form_com,
               'attachments':attachments,
               'comments':comments}
    
    if request.method == 'POST':
        if 'update_project' in request.POST:
            form = ProjectForm(request.POST, instance=project)
            form.save()

            comment = request.POST.get('comment')
            if comment.strip() != '':
                com = Comment(name=comment[:20], comment=comment, project_id=project_id)
                com.save()

            form_com = CommentForm(request.POST)
            files = request.FILES.getlist('file')
            for fl in files:
                att = Attachment(name=str(fl), file=fl, project_id=project_id)
                att.save()
            
        elif 'remove_project' in request.POST:
            id = request.POST.get("project_id")
            removeAttachmentFilesBatch(id)
            Project.objects.filter(id=id).delete()
            # Attachment.objects.filter(project_id=id).delete()
        return redirect('app:projects')
    else:
        return render(request, 'app/single-project.html', context)
    
def archive_project(request, project_id):
    project = Project.objects.filter(pk=project_id)
    project.update(archived=True, archivedate=datetime.datetime.now())
    return redirect('app:projects')

def removeAttachmentFilesBatch(projectID):
    attachments = Attachment.objects.filter(project_id=projectID)

    for att in attachments:
        fileName = settings.MEDIA_ROOT + '/' + str(att.file)
        if os.path.exists(fileName):
            os.remove(fileName)

def remove_attachment(request, project_id, attachment_id):
    att = Attachment.objects.filter(project_id=project_id).filter(pk=attachment_id)
    file_name = settings.MEDIA_ROOT + '/' + str(att[0].file)

    att.delete()
    
    if os.path.exists(file_name):
        os.remove(file_name)

    return redirect('app:single-project', project_id=project_id)

def remove_comment(request, project_id, comment_id):
    com = Comment.objects.filter(project_id=project_id).filter(pk=comment_id)

    com.delete()

    return redirect('app:single-project', project_id=project_id)
