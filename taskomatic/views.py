from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from datetime import datetime
from .forms import ProjectForm, TaskForm, InventoryForm, CompletionTaskForm, CommentForm
import json

from .models import User, Project, Tasks, Inventory, Relationship, Member, Notification, Comment


def index(request):
    if request.user.is_authenticated:

        # Retrieve relevant data
        currentUserId = request.user.id
        currentUser = User.objects.get(id=currentUserId)
        projects = Project.objects.filter(user=currentUser).order_by('-creationDate')
        contacts = Relationship.objects.filter(Q(from_user=currentUser) | Q(to_user=currentUser), ~Q(status='rejected'))
        contactRequests = Relationship.objects.filter(Q(to_user=currentUser), Q(status="pending"))
        memberProjects = Member.objects.filter(user=currentUser)
        notifications = Notification.objects.filter(user=currentUser)

        # Create a context dictionary with the retrieved data
        context = {
            "projects": projects,
            "memberProjects": memberProjects,
            "contacts": contacts,
            "contactRequests": contactRequests,
            "notifications": notifications 
        }

        return render(request, "taskomatic/index.html", context)
    return render(request, "taskomatic/index.html")


def users_view(request):

    # Retrieve relevant data
    q = request.GET.get('q', '')
    currentUserId = request.user.id
    currentUser = User.objects.get(id=currentUserId)
    users = User.objects.filter(Q(username__icontains=q), ~Q(username=currentUser))
    relationship = Relationship.objects.filter(Q(from_user=currentUser) | Q(to_user=currentUser))

    # Create dictionaries and store the relationship status (accepted or pending) for each user
    acceptedRelationshipStatus = {}
    pendingRelationshipStatus = {}
    for relation in relationship:
        if relation.status == 'pending':
            if currentUser == relation.from_user:
                user = str(relation.to_user)
                pendingRelationshipStatus[user] = relation.status
            elif currentUser == relation.to_user:
                user = str(relation.from_user)
                pendingRelationshipStatus[user] = relation.status
        elif relation.status == 'accepted':
            if currentUser == relation.from_user:
                user = str(relation.to_user)
                acceptedRelationshipStatus[user] = relation.status
            elif currentUser == relation.to_user:
                user = str(relation.from_user)
                acceptedRelationshipStatus[user] = relation.status

    # Create a context dictionary with the retrieved data          
    context = {
        "users": users,
        "acceptedRelationshipStatus": acceptedRelationshipStatus,
        "pendingRelationshipStatus": pendingRelationshipStatus
    }

    return render(request, "taskomatic/users.html", context)


def add_contact(request, pk):

    # Get the user that the current user wants to add as a contact
    to_user = User.objects.get(id=pk)
    currentUserId = request.user.id
    from_user = User.objects.get(id=currentUserId)

    # Create a new Relationship object with a status of "pending"
    relationship = Relationship(from_user=from_user, to_user=to_user, status='pending')
    relationship.save()

    # Redirect the user back to the page they were on
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def accept_contact(request, pk):

    #Retrieve and Update the relationship
    relationshipToUpdate = Relationship.objects.get(id=pk)
    relationshipToUpdate.status = "accepted"
    relationshipToUpdate.save()

    return HttpResponseRedirect(reverse("index"))


def reject_contact(request, pk):

    #Retrieve and Update the relationship
    relationshipToUpdate = Relationship.objects.get(id=pk)
    relationshipToUpdate.status = "rejected"
    relationshipToUpdate.save()

    return HttpResponseRedirect(reverse("index"))


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

    # Retrieve relevant data
    project = Project.objects.get(id=pk)
    tasks = Tasks.objects.filter(projectId = pk)
    inventory = Inventory.objects.filter(projectId = pk)
    comments = Comment.objects.filter(project=project).order_by('-id')

    # Form for task completion checkboxes
    taskForms = []
    for task in tasks:
        taskFormInstance = CompletionTaskForm(instance=task, task_id=task.id)
        taskForms.append(taskFormInstance)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            currentUserId = request.user.id
            currentUser = User.objects.get(id=currentUserId)  
            f = Comment(project=project, user=currentUser, comment=form.cleaned_data['comment'], date=datetime.now().strftime("%Y-%m-%d"), time=datetime.now().strftime("%H:%M"))
            f.save()   

    # Create a context dictionary with the retrieved data
    context = {
        'project': project,
        'tasks': tasks,
        'inventory': inventory,
        'comments': comments,
        'taskForm': TaskForm(),
        'taskForms': taskForms,
        'inventoryForm': InventoryForm(),
        'form': CommentForm()
    }

    return render(request, "taskomatic/projectPage.html", context)


def new_project(request):
    user = User.objects.get(username=request.user)
    if request.method == "POST":
        print('NEW PAGE HERE')
        # Form validation
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

        try: 

            # Update Project data
            projectCreationDate = request.POST['projectCreationDate']
            projectId = request.POST['projectId']
            projectInstance = Project.objects.get(id=projectId)
            form = ProjectForm(request.POST, instance=projectInstance)

            if form.is_valid():
                cleaned_data = form.cleaned_data
                projectInstance.user = cleaned_data['user']
                projectInstance.owner = cleaned_data['owner']
                projectInstance.projectName = cleaned_data['projectName']
                projectInstance.projectDescription = cleaned_data['projectDescription']
                projectInstance.hasDeadline = cleaned_data['hasDeadline']
                projectInstance.hasTasks = cleaned_data['hasTasks']
                projectInstance.hasInventory = cleaned_data['hasInventory']
                projectInstance.creationDate = projectCreationDate
                projectInstance.deadlineDate = cleaned_data['deadlineDate']
                projectInstance.save()
                print('Project Updated!')

            return HttpResponseRedirect(reverse("index"))   
        except:

            # Retrieve data and pre-populate form
            projectId = request.POST['projectId']
            projectInstance = Project.objects.get(id=projectId)
            form = ProjectForm(instance=projectInstance)
            creationDate = str(projectInstance.creationDate)
            print(creationDate)

            return render(request, "taskomatic/newProject.html", {
            "projectId": projectId,
            "projectCreationDate": creationDate,
            "form": form
            })

    return render(request, "taskomatic/register.html")


def delete_project(request):
    if request.method == "POST":

        projectId = request.POST['toDeleteProjectId']
        projectToDelete = Project.objects.get(id=projectId)

        # Verify ownership of project
        if str(request.user) == projectToDelete.owner:
            projectToDelete.delete()

            return HttpResponseRedirect(reverse("index"))
        
    return HttpResponseRedirect(reverse("register"))


def handle_tasks(request, action, pk=0):
    if request.method == "POST":

        # Evaluate the action and perform operation accordingly
        if action == 'add':
            form = TaskForm(request.POST)
            if form.is_valid():
                f = Tasks(projectId=form.cleaned_data['projectId'], taskCreator=form.cleaned_data['taskCreator'], taskName=form.cleaned_data['taskName'],
                          taskDescription=form.cleaned_data['taskDescription'], taskDeadline=form.cleaned_data['taskDeadline'], taskLimitAlert=form.cleaned_data['taskLimitAlert'], 
                          taskImportance=form.cleaned_data['taskImportance'], taskCompletion=form.cleaned_data['taskCompletion'], taskCreationDate=datetime.now().strftime("%Y-%m-%d"))
                f.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                print(form.errors)

        elif action == 'delete':

            taskInstance = Tasks.objects.get(id=pk)
            if taskInstance:
                print(f'deleting task id: {pk}')
                taskInstance.delete()
            else:
                print('Task not found')

        elif action == 'complete':
            task_id = request.POST.get('taskCompletion')
            if task_id:
                task = Tasks.objects.get(id=task_id)
            else:
                task_id = request.POST['hidTaskId']
                task = Tasks.objects.get(id=task_id)
            if not(task.taskCompletion):
                task.taskCompletion = True
            else:
                task.taskCompletion = False
            task.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        else:
            print('Invalid operation')

    return HttpResponseRedirect(reverse("index"))


def handle_inventory(request, action, pk=0):
    print(pk)
    if request.method == "POST":

        # Evaluate the action and perform operation accordingly
        if action == 'add':
            form = InventoryForm(request.POST)
            if form.is_valid():
                f = Inventory(projectId=form.cleaned_data['projectId'], itemName=form.cleaned_data['itemName'], itemDescription=form.cleaned_data['itemDescription'],
                              itemQty=form.cleaned_data['itemQty'], itemUnit=form.cleaned_data['itemUnit'], itemLimitAlert=form.cleaned_data['itemLimitAlert'])
                f.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                print('Something went wrong')
                print(form.errors)

        elif action == 'increment':
            if pk:
                item = Inventory.objects.get(id=pk)
                item.itemQty += 1
                item.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))   
            
        elif action == 'decrement':  
            if pk:
                item = Inventory.objects.get(id=pk)
                item.itemQty -= 1
                item.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    
             
        elif action == 'edit':
            if pk:
                item = Inventory.objects.get(id=pk)
                updateInventoryForm = InventoryForm(instance=item)
                currentItemId = item.id
                currentProjectId = item.projectId.id

                context = {
                    "currentProjectId": currentProjectId,
                    "currentItemId": currentItemId,
                    'inventoryForm': updateInventoryForm
                }

                inventoryPage_html = render(request, "taskomatic/inventoryForm.html", context).content.decode('utf-8')
                
                return JsonResponse({'inventoryPage_html': inventoryPage_html})
            
            else:
                itemId = request.POST['itemId']
                itemInstance = Inventory.objects.get(id=itemId)
                form = InventoryForm(request.POST, instance=itemInstance)

                if form.is_valid():
                    cleaned_data = form.cleaned_data
                    itemInstance.itemName = cleaned_data['itemName']
                    itemInstance.itemDescription = cleaned_data['itemDescription']
                    itemInstance.itemQty = cleaned_data['itemQty']
                    itemInstance.itemUnit = cleaned_data['itemUnit']
                    itemInstance.itemLimitAlert = cleaned_data['itemLimitAlert']
                    itemInstance.save()
                    print('Inventory Item Updated!')

                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                
                else:
                    print('Something went wrong')
                    print(form.errors)

        elif action == 'delete':
            itemInstance = Inventory.objects.get(id=pk)
            if itemInstance:
                print(f'deleting item id: {pk}')
                itemInstance.delete()
            else:
                print('Item not found')

        else:
            print('Invalid operation')
    
    
    return HttpResponseRedirect(reverse("index"))


def add_member(request, projectId):
    if request.user.is_authenticated:

        # Retrieve relevant data
        currentProjectId = projectId
        currentUserId = request.user.id
        currentProject = Project.objects.get(id=currentProjectId)
        currentUser = User.objects.get(id=currentUserId)
        users = User.objects.filter(~Q(username=currentUser))
        members = Member.objects.filter(project=currentProject)
        relationship = Relationship.objects.filter(Q(from_user=currentUser) | Q(to_user=currentUser))

        # Create dictionaries and get relationship status
        acceptedRelationshipStatus = {}
        pendingRelationshipStatus = {}
        currentMembers = {}
        for relation in relationship:
            if relation.status == 'pending':
                if currentUser == relation.from_user:
                    user = str(relation.to_user)
                    pendingRelationshipStatus[user] = relation.status
                elif currentUser == relation.to_user:
                    user = str(relation.from_user)
                    pendingRelationshipStatus[user] = relation.status
            elif relation.status == 'accepted':
                if currentUser == relation.from_user:
                    user = str(relation.to_user)
                    acceptedRelationshipStatus[user] = relation.status
                elif currentUser == relation.to_user:
                    user = str(relation.from_user)
                    acceptedRelationshipStatus[user] = relation.status
        for member in members:
            memberInstance = str(member.user.username)
            currentMembers[memberInstance] = True

        context = {
        "users": users,
        "acceptedRelationshipStatus": acceptedRelationshipStatus,
        "pendingRelationshipStatus": pendingRelationshipStatus,
        "members": currentMembers,
        "project": currentProject
    }

        if request.method == "POST":

            try:
                # Post incoming from membersPage contains json data that is used for toggling members access
                requestData = json.loads(request.body)
            except:
                # Post incoming from dashboard is redirected here and removes user from project
                f = Member.objects.get(Q(project=currentProject), Q(user=currentUser))
                f.delete()
                print('Member removed!')
                return HttpResponseRedirect(reverse("index"))
            
            memberUser = requestData.get("username")
            print(memberUser)
            memberUserInstance = User.objects.get(username=memberUser)
            print(memberUser)
            if memberUser not in currentMembers:
                f = Member(project=currentProject, user=memberUserInstance)
                f.save()
                print('Member added!')
                n = Notification(user=memberUserInstance, notification=f"You have been added to {currentProject.projectName} project")
                n.save()
            else:
                f = Member.objects.get(Q(project=currentProject), Q(user=memberUserInstance))
                f.delete()
                print('Member removed!')
        
        return render(request, "taskomatic/membersPage.html", context)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

def dismiss_notification(request):
    if request.method == "POST":

        #Retrieve notification ID
        requestData = json.loads(request.body)
        notificationId = requestData.get("notificationId")

        #Dismiss notification
        notification = Notification.objects.get(id=notificationId)
        notification.delete()

        return HttpResponse('notification dismissed')