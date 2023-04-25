from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput

from .models import User, Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            'projectName': TextInput(attrs={
            'class': "max-w-lg rounded border px-3 py-[0.32rem] mb-1",
            'id': "projectTitleInput",
            'placeholder': "Project Title"
            }),
            'projectDescription': Textarea(attrs={
            'class': 'rounded px-3 py-[0.32rem] m-2',
            'cols': "60",
            'rows': "6",
            'id': 'projectDescriptionInput',
            'placeholder': "Project Description"
            }),
            'hasTasks': CheckboxInput(),
            'hasInventory': CheckboxInput(),
            'hasDeadline': CheckboxInput(attrs={
            'id': "projectTitleInput"
            })
        }

def index(request):
    return render(request, "taskomatic/index.html")


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
    form = ProjectForm(request.POST)
    return render(request, "taskomatic/newProject.html", {
        "form": ProjectForm()
    })