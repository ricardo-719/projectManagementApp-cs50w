from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, DateInput, NumberInput, HiddenInput

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
            "projectId": HiddenInput(),
            "taskCreator": HiddenInput(),
            "taskName": TextInput(attrs={
            'class': "max-w-lg rounded border px-3 py-[0.32rem] mb-1 ml-2",
            'id': 'addTaskModalFormTitle',
            'placeholder': "Project Title"
            }),
            "taskDescription": Textarea(attrs={
            'class': 'rounded border px-3 py-[0.32rem] m-2',
            'id': 'addTaskModalFormDescription',
            'rows': "6",
            'placeholder': "Task details"
            }),
            'taskDeadline': DateInput(attrs=dict(type='date')),
            'taskLimitAlert': DateInput(attrs=dict(type='date'))
        }

class InventoryForm(ModelForm):

    class Meta:
        model = Inventory
        fields = "__all__"
        widgets = {
            "projectId": HiddenInput(),
            "itemName": TextInput(attrs={
            'class': "max-w-lg rounded border px-3 py-[0.32rem] mb-1 ml-2",
            'id': 'addInventoryModalFormTitle',
            'placeholder': "Item Name"
            }),
            "itemDescription": Textarea(attrs={
            'class': 'rounded border px-3 py-[0.32rem] m-2',
            'id': 'addInventoryModalFormDescription',
            'rows': "6",
            'placeholder': "Item Notes"
            }),
            'itemQty': NumberInput(attrs={
                'class': "border",
                'placeholder': "Amount"
            }),
            'itemLimitAlert': NumberInput(attrs={
                'class': "border mt-3",
                'placeholder': "Restock Limit"
            })
        }
