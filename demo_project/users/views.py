from django.shortcuts import render, redirect  
from django.http import HttpResponse 
from .models import Profile
from django.contrib.auth.models import User 
from django.contrib.auth import login,authenticate, logout  
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
from .form import CustomUserCreationForm ,SkillsForm , MessageForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .utils import searchProfiles ,paginateProfiles


def home(request):
    return render(request, 'users/home.html')

def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.object.get(username=username)
        except:
            messages.warning(request,'username or password does not exist')
        user = authenticate(request,username=username, password=password)    
            
        if user is not None:
            login(request, user)
            #messages.success(request,'Hello welcome ')
            return redirect('profile')  
    context = {'page':page}              
    return render(request, 'users/login_user.html',context) 


def logoutUser(request):
    logout(request)
    messages.error(request,'successfully logged out')
    return redirect('login') 


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.username = user.username.lower()
           user.save()
           return redirect('login') 
    context = {'page':page, 'form':form}
    return render(request,'users/login_user.html',context)

def profile(request):
    profile, search_query = searchProfiles(request)
    page = request.GET.get('page') 
    results = 2
    paginator = Paginator(profile,results)
    try:
        profile = paginator.page(page)
    except PageNotAnInteger:
        page = 1    
        profile = paginator.page(page) 
    except EmptyPage:
        page = paginator.num_pages
        profile = paginator.page(page)     
    #custom_range = paginateProfiles(request,profile,3)
    #profiles = Profile.objects.all()
    context = {'profiles': profile, 
               'search_query': search_query,
               'paginator': paginator}
               #'custom_range': custom_range} 
    return render(request,'users/profile.html',context) 


def detailProfile(request,pk):
    profiles = Profile.objects.get(id=pk)
    context = {'profiles': profiles } 
    return render(request,'users/detail_profile.html',context) 

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    project = profile.project_set.all()
    context = {'profile': profile, 'skills': skills, 'project': project }
    return render(request,'users/user_account.html',context)


@login_required(login_url='login')
def createSkills(request):
    profile = request.user.profile
    form = SkillsForm()
    if request.method == 'POST':
        form = SkillsForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile 
            skill.save()
            return redirect('user-account')
    context = {'form':form} 
    return render(request,'users/create_skills.html',context) 


@login_required(login_url='login')
def updateSkills(request,pk):
    profile = request.user.profile
    updateObj = profile.skill_set.get(id=pk)
    form = SkillsForm(instance=updateObj)
    if request.method == 'POST':
        form = SkillsForm(request.POST, instance=updateObj)
        if form.is_valid:
            form.save()
            return redirect('user-account')
    context = {'form':form} 
    return render(request,'users/create_skills.html',context) 


@login_required(login_url='login')
def deleteSkills(request,pk):
    profile = request.user.profile
    deleteObj = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        deleteObj.delete()
        return redirect('user-account') 
    context = {'deleteObj':deleteObj}
    return render(request,'users/delete_skills.html',context)  


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequest = profile.messages.all()
    unreadCount = messageRequest.filter(is_read=False).count()
    context = {'messageRequest':messageRequest, 'unreadCount': unreadCount}
    return render(request,'users/inbox.html',context)


@login_required(login_url='login')
def viewMessage(request,pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {'message':message}
    return render(request,'users/message.html',context) 


@login_required(login_url='login')
def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    context = {'form':form, 'recipient':recipient}
    return render(request,'users/message_form.html',context)
    
    
    
    
    