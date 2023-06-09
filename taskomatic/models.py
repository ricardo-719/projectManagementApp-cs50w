from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    pass

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.CharField(max_length=80)
    projectName = models.CharField(max_length=160)
    projectDescription = models.CharField(max_length=350)
    hasDeadline = models.BooleanField(default=False)
    hasInventory = models.BooleanField(default=False)
    hasTasks = models.BooleanField(default=False)
    creationDate = models.DateField(null=True, blank=True)
    deadlineDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.projectName} created by {self.user}"

class Member(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Inventory(models.Model):
    UNITS_CATEGORIES = [
        ('UNIT', 'unit(s)'),
        ('%', 'percent'),
        ('KG', 'kilogram(s)'),
        ('CM', 'centimeter(s)')
    ]
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=160)
    itemDescription = models.CharField(max_length=350)
    itemQty = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    itemUnit = models.CharField(max_length=20, choices=UNITS_CATEGORIES, default=UNITS_CATEGORIES[0][0])
    itemLimitAlert = models.IntegerField(null=True, blank=True)

class Tasks(models.Model):
    PRIORITY_LEVELS = [tuple([x,x]) for x in range(1,11)]

    projectId = models.ForeignKey(Project, on_delete=models.CASCADE)
    taskCreator = models.CharField(max_length=80)
    taskName = models.CharField(max_length=160)
    taskDescription = models.CharField(max_length=350)
    taskCompletion = models.BooleanField(default=False)
    taskDeadline = models.DateField(null=True, blank=True)
    taskImportance = models.PositiveIntegerField(default=PRIORITY_LEVELS[0], choices=PRIORITY_LEVELS, validators=[MinValueValidator(1), MaxValueValidator(10)])
    taskLimitAlert = models.DateField(null=True, blank=True)
    taskCreationDate = models.DateField(null=True, blank=True)

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

class Relationship(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f"{self.from_user} | {self.to_user} | {self.status}" 

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.CharField(max_length=100)

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=280)
    date = models.DateField()
    time = models.TimeField()