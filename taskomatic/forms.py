from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, DateInput, NumberInput

from .models import Project, Tasks, Inventory

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
                'id': "projectDeadlineCheckbox",
                'name': "projectDeadlineCheckbox"
            }),
            'deadlineDate': DateInput(attrs=dict(type='date'))
        }

class TaskForm(ModelForm):

    class Meta:
        model = Tasks
        fields = "__all__"
        widgets = {
            "taskName": TextInput(attrs={
            'class': "max-w-lg rounded border px-3 py-[0.32rem] mb-1",
            'id': 'addTaskModalFormTitle',
            'placeholder': "Project Title"
            }),
            "taskDescription": Textarea(attrs={
            'class': 'rounded px-3 py-[0.32rem] m-2',
            'id': 'addTaskModalFormDescription',
            'rows': "6",
            'placeholder': "Task details"
            }),
            'itemQty': NumberInput(attrs={
                'placeholder': "Amount"
            })
        }

class InventoryForm(ModelForm):

    class Meta:
        model = Inventory
        fields = "__all__"
        widgets = {
            "itemName": TextInput(attrs={
            'class': "max-w-lg rounded border px-3 py-[0.32rem] mb-1",
            'id': 'addInventoryModalFormTitle',
            'placeholder': "Project Title"
            }),
            "itemDescription": Textarea(attrs={
            'class': 'rounded px-3 py-[0.32rem] m-2',
            'id': '#addInventoryModalFormDescription',
            'rows': "6",
            'placeholder': "Item notes"
            })
        }
