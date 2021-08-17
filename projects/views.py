from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProjectForm,ReviewForm
from .models import Project, Review
from django.contrib.auth.decorators import login_required
from .utils import searchProject,paginateData
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
# Create your views here.


def projects(request):
    projects,search_query=searchProject(request)
    custom_range,projects=paginateData(request,projects,6) 
    context = {'projects':projects,'search_query':search_query,"custom_range":custom_range}
    return render(request,'projects/projects.html',context)


def project(request,pk):
    projectobj=Project.objects.get(id=pk)
    tags=projectobj.tags.all()
    reviews=projectobj.review_set.all()
    form=ReviewForm()
    if request.method == 'POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.owner=request.user.profile
            review.project=projectobj
            review.save()
            messages.success(request,"review submitted ")
            projectobj.getVoteCount
            return redirect('project',pk=projectobj.id)
    print(projectobj.reviewers)
    context={'project':projectobj,'tags':tags,'reviews':reviews,'form':form}
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