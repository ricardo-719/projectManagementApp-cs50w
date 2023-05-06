from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from .forms import ProjectForm, TaskForm, InventoryForm
from . import urls

from .models import User, Project, Tasks, Inventory

def index(request):
    projects = Project.objects.all().order_by('-creationDate')
    return render(request, "taskomatic/index.html", {
        "projects": projects
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "taskomatic/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "taskomatic/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "taskomatic/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "taskomatic/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "taskomatic/register.html")


def project_view(request, pk):
    project = Project.objects.filter(id=pk)
    tasks = Tasks.objects.filter(projectId = pk)
    inventory = Inventory.objects.filter(projectId = pk)
    return render(request, "taskomatic/projectPage.html", {
        'project': project,
        'tasks': tasks,
        'inventory': inventory,
        'taskForm': TaskForm(),
        'inventoryForm': InventoryForm()
    })


def new_project(request):
    user = User.objects.get(username=request.user)
    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            f =  Project(user=form.cleaned_data['user'], owner=form.cleaned_data['owner'], projectName=form.cleaned_data['projectName'], 
                         projectDescription=form.cleaned_data['projectDescription'], hasTasks=form.cleaned_data['hasTasks'], 
                         hasInventory=form.cleaned_data['hasInventory'], hasDeadline=form.cleaned_data['hasDeadline'], 
                         deadlineDate=form.cleaned_data['deadlineDate'], creationDate=datetime.now().strftime("%Y-%m-%d"))
            f.save()
        else:
            print(form.errors)

        return HttpResponseRedirect(reverse("index"))
    return render(request, "taskomatic/newProject.html", {
        "form": ProjectForm(),
        "user": user
    })


def edit_project(request):
    if request.method == "POST":
        projectId = request.POST['projectId']
        projectInstance = Project.objects.get(id=projectId)
        form = ProjectForm(instance=projectInstance)
        return render(request, "taskomatic/newProject.html", {
        "form": form
        })
    return render(request, "taskomatic/register.html")


def delete_project(request):
    if request.method == "POST":
        projectId = request.POST['toDeleteProjectId']
        projectToDelete = Project.objects.get(id=projectId)

        # Verify ownership
        if str(request.user) == projectToDelete.owner:
            projectToDelete.delete()
            return HttpResponseRedirect(reverse("index"))
        
    return HttpResponseRedirect(reverse("register"))


def handle_tasks(request, action):
    if request.method == "POST":
        if action == 'add':
            form = TaskForm(request.POST)
            
            if form.is_valid():
                f = Tasks(projectId=form.cleaned_data['projectId'], taskCreator=form.cleaned_data['taskCreator'], taskName=form.cleaned_data['taskName'],
                          taskDescription=form.cleaned_data['taskDescription'], taskDeadline=form.cleaned_data['taskDeadline'], taskLimitAlert=form.cleaned_data['taskLimitAlert'], 
                          taskImportance=form.cleaned_data['taskImportance'], taskCreationDate=datetime.now().strftime("%Y-%m-%d"))
                f.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                print(form.errors)

        elif action == 'edit':
            print('editing...')
        elif action == 'delete':
            print('deleting...')
        else:
            print('Invalid Operation...')
    return HttpResponseRedirect(reverse("index"))


def handle_inventory(request):
    if request.method == "POST":
        action = request.POST['action']
        if action == 'add':
            print('adding...')
        elif action == 'edit':
            print('editing...')
        elif action == 'delete':
            print('deleting...')
        else:
            print('Something went wrong...')
    return HttpResponseRedirect(reverse("index"))