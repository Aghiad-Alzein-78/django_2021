from django.db.models import Q
from .models import Project
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def searchProject(request):
    search_query=""
    if request.GET.get("search_query"):
        search_query=request.GET.get("search_query")
    projects=Project.objects.distinct().filter(
        Q(title__icontains=search_query)|
        Q(description__icontains=search_query)|
        Q(owner__name__icontains=search_query)|
        Q(tags__name__icontains=search_query)
        )
    return projects,search_query

def paginateData(request,projects,results):
    paginator=Paginator(projects,results)

    page=request.GET.get("page")
    try:
        projects=paginator.page(page)
    except PageNotAnInteger:
        page=1
        projects=paginator.page(page)
    except EmptyPage:
        page=1
        projects=paginator.page(page)
    
    leftIndex=int(page)-2
    if leftIndex<1:
        leftIndex=1
    rightIndex=int(page)+2
    if rightIndex>paginator.num_pages:
        rightIndex=paginator.num_pages
    custom_range=range(leftIndex,rightIndex+1)
    return custom_range,projects