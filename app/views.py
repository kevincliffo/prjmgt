from django.shortcuts import render, redirect
import datetime
from .forms import AttachmentForm
from .models import Project, Attachment

def index(request):
    context = {'year':datetime.datetime.now().year}
    return render(request, 'app/index.html', context)

def login(request):
    context = {'year':datetime.datetime.now().year}
    print('request.method : ' + request.method)
    if request.method == 'POST':
        return redirect('app:dashboard')
    else:
        return render(request, 'app/index.html', context)

def logout(request):
    return redirect('app:index')

def dashboard(request):
    context = {'year':datetime.datetime.now().year}
    return render(request, 'app/dashboard.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {'year':datetime.datetime.now().year,
               'projects':projects}
    return render(request, 'app/projects.html', context)

def add_project(request):
    if request.method == 'POST':
        projectName = request.POST.get('projectName')
        projectOwner = request.POST.get('projectOwner')
        projectDescription = request.POST.get('projectDescription')
        language = request.POST.get('language')
        startDate = request.POST.get('startDate')
        status = request.POST.get('status')
        finishedDate = request.POST.get('finishedDate')

        frmProject = Project(name=projectName, description=projectDescription, owner=projectOwner, startdate=startDate, 
                             language=language, status=status, finishdate=finishedDate)
        #frmProject.save()
        frmProject.save()

        prj = Project.objects.filter(name=projectName)
        print(projectName)
        f = open('test.txt', 'w')
        files = request.FILES.getlist('file')
        for fl in files:
            f.writelines(str(fl) + '\n')
            att = Attachment(name=str(fl), file=fl, project_id=prj[0].id)
            att.save()
        f.close()
        print(files)
        return redirect('app:add_project')
    else:
        form = AttachmentForm()
        context = {'year':datetime.datetime.now().year,
                   'form':form}

        return render(request, 'app/add_project.html', context)

def single_project(request, project_id):
    project = Project.objects.get(pk=project_id)

    attachments = Attachment.objects.filter(project_id=project_id)

    status = ['No Started', 'Started', 'In Progress', 'Halted', 'Finished']
    languages = ['Android', 'Angular','C Shart','Django','Flask','Flutter','Ionic',
                 'Java','Javascript','Kotlin','Laravel','PHP','Python','React','VueJS','Yii']

    context = {'project' : project,
               'attachments':attachments,
               'status':status,
               'languages':languages}
    return render(request, 'app/single_project.html', context)
    
def update_project(request, project_id):
    project = Project.objects.get(pk=project_id)

    attachments = Attachment.objects.filter(project_id=project_id)
    context = {'project' : project,
               'attachments':attachments}
    return render(request, 'app/single_project.html', context)       