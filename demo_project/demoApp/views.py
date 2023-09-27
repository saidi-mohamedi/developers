from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .form import ProjectForm ,ReviewForm 
from .models import Project, Tag  
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .utils import searchProject, paginateProjects  

def dashboard(request):
    project, search_query = searchProject(request) 
    custom_range,project = paginateProjects(request,project, 2)      
    context = {'project':project, 'search_query': search_query,
                'custom_range': custom_range }
    return render(request, 'demoApp/dashboard.html', context)  
    
def index(request,pk): 
    project = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project 
        review.owner = request.user.profile
        review.save()
        project.getVoteCount
        #messages.success(request,'Your review was successfully submitted!')
        return redirect('index', pk=project.id)
    context = {'project':project, 'form':form} 
    return render(request, 'demoApp/index.html',context) 

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile 
    form = ProjectForm() 
    if  request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split() 
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile 
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('user-account')
    context = {'form':form}
    return render(request, 'demoApp/project_form.html', context)  





@login_required(login_url="login")
def updateProject(request,pk):
    profile = request.user.profile
    updateproject = profile.project_set.get(id=pk)
    form = ProjectForm(instance=updateproject) 
    if  request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split() 
        form = ProjectForm(request.POST,request.FILES,instance=updateproject)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('user-account')
    context = {'form':form}
    return render(request, 'demoApp/project_form.html', context)  


@login_required(login_url="login")
def deleteProject(request,pk):
    profile = request.user.profile
    deleteproject = profile.project_set.get(id=pk)
    if  request.method == 'POST':
        deleteproject.delete()
        return redirect('dashboard')
    context = {'deleteproject':deleteproject}
    return render(request, 'demoApp/delete.html', context)  
