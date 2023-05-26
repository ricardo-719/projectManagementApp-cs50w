from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users", views.users_view, name="users"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("newProject", views.new_project, name="newProject"),
    path("editProject", views.edit_project, name="editProject"),
    path("deleteProject", views.delete_project, name="deleteProject"),
    path("handleTasks/<str:action>", views.handle_tasks, name="handleTasks"),
    path("handleInventory/<str:action>/<int:pk>", views.handle_inventory, name="handleInventory"),
    path("handleInventory/<str:action>", views.handle_inventory, name="handleInventory"),
    path("project/<str:pk>/", views.project_view, name="projectPage"),
    path("accept/<str:pk>/", views.accept_contact, name="acceptContact"),
    path("reject/<str:pk>/", views.reject_contact, name="rejectContact"),
    path("users/<str:pk>/", views.add_contact, name="addContact")
]