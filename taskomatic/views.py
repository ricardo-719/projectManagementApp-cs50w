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
    

def new_project(request):
    if request.method == "POST":
        pName = request.POST['projectName']
        pDescription = request.POST['projectDescription']
        hTasks = request.POST.get('hasTasks', False)
        hInventory = request.POST.get('hasInventory', False)
        hDeadline = request.POST.get('hasDeadline', False)
        dDate = request.POST['deadlineDate']
        if hTasks == 'on': hTasks = True
        if hInventory == 'on' : hInventory = True
        if hDeadline == 'on' : hDeadline = True
        if dDate == "": dDate = None  

        f =  Project(user=request.user, owner=request.user, projectName=pName, projectDescription=pDescription, hasTasks=hTasks, hasInventory=hInventory, hasDeadline=hDeadline, deadlineDate=dDate, creationDate=datetime.now().strftime("%Y-%m-%d"))
        f.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "taskomatic/newProject.html", {
        "form": ProjectForm()
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

def delete_project(request):
    if request.method == "POST":
        projectId = request.POST['toDeleteProjectId']
        # TODO: Add authentication based on ownership
        projectToDelete = Project.objects.get(id=projectId)
        projectToDelete.delete()
        return HttpResponseRedirect(reverse("index"))
    return HttpResponseRedirect(reverse("register"))