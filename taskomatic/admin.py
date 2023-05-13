from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Project, Inventory, Tasks, Relationship, Room, Message

admin.site.register(User, UserAdmin)
admin.site.register(Project)
admin.site.register(Tasks)
admin.site.register(Inventory)
admin.site.register(Relationship)
admin.site.register(Room)
admin.site.register(Message)
