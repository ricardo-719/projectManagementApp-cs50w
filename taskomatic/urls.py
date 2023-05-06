from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("newProject", views.new_project, name="newProject"),
    path("editProject", views.edit_project, name="editProject"),
    path("deleteProject", views.delete_project, name="deleteProject"),
    path("handleTasks/<str:action>", views.handle_tasks, name="handleTasks"),
    path("handleInventory/<str:action", views.handle_inventory, name="hamdleInventory"),
    path("project/<str:pk>/", views.project_view, name="projectPage")
]