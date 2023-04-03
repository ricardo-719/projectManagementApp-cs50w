from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    pass

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=80)
    projectName = models.CharField(max_length=160)
    projectDescription = models.CharField(max_length=350)
    hasDeadline = models.BooleanField(default=False)
    hasInventory = models.BooleanField(default=False)
    hasTasks = models.BooleanField(default=False)
    creationDate = models.DateField()
    deadlineDate = models.DateField(null=True, blank=True)

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
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE)
    taskName = models.CharField(max_length=160)
    taskDescription = models.CharField(max_length=350)
    taskDeadline = models.DateField(null=True, blank=True)
    taskImportance = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    taskLimitAlert = models.DateField(null=True, blank=True)