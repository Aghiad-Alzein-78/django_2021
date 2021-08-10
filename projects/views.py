from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProjectForm
from .models import Project
from django.contrib.auth.decorators import login_required
from .utils import searchProject
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.


def projects(request):
    projects,search_query=searchProject(request)
    p=Paginator(projects,1000)
    page=request.GET.get('page')
    try:
        projects=p.page(page)
    except PageNotAnInteger:
        page=1
        projects=p.page(page)
    except EmptyPage:
        page=p.num_pages
        projects=p.page(page)
    context = {'projects':projects,'search_query':search_query,'paginator':p}
    return render(request,'projects/projects.html',context)


def project(request,pk):
    projectobj=Project.objects.get(id=pk)
    tags=projectobj.tags.all()
    context={'project':projectobj,'tags':tags}
    return render(request,'projects/single-project.html',context)

@login_required(login_url='login')
def createProject(request):
    form=ProjectForm()
    profile=request.user.profile
    if request.method == 'POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            return redirect('account')
    context={'form':form}
    return render(request,'projects/project_form.html',context)

    
@login_required(login_url='login')
def updateProject(request,pk):
    profile=request.user.profile
    project=profile.project_set.get(id=pk)
    form=ProjectForm(instance=project)
    if request.method=="POST":
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return  redirect('account')
    context={'form':form}
    return render(request,'projects/project_form.html',context)


@login_required(login_url='login')
def deleteProject(request,pk):
    profile=request.user.profile
    project=profile.project_set.get(id=pk)
    context={'object':project.title}
    if request.method=="POST":
        project.delete()
        return redirect('projects')
    return render(request,'delete_template.html',context)