from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

projectList=[
    {
        'id':'1',
        'title':'Ecommerce Website',
        'description':'Fully functional ecommerce website'
    },
    {
        'id':'2',
        'title':'Portfolio Website',
        'description':'This is a portofolio Website'
    },
    {
        'id':'3',
        'title':'Social Network',
        'description':'Awsome open source project I am still working'
    }
]

def projects(request):
    page="projects"
    number=9
    context = {'page':page,'number':number,'projects':projectList}
   
    return render(request,'projects/projects.html',context)


def project(request,pk):
    projectobj=None
    for i in projectList:
        if i['id']==pk:
            projectobj=i
    context={''}
    return render(request,'projects/single-project.html',{'project':projectobj})
