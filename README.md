# Task-o-Matic

A web-app for project management where the user is able to keep track of things such as deadlines, tasks and inventories. The application will alert according to user specifications and different views will provide overall information about one or more projects. Teams can be created with shared information, with the option of setting a Project Manager to follow-up on each of the team members, suggests tasks and set deadlines, etc.

## Files:

- index.html...
- views.py...
    edit_project: Takes the project's id as an argument and pre-fill forms for editing the project.
    delete_project: Takes the project's id through a POST request and updates the database by deleting the corresponding project.
- models.py...
- forms.py : this file contains all ModelForms of the project. The purpose is to have a better organized project by separation of concerns and in this way not having to rely on the views.py the manage things related to the forms. 
- newProject.html...
- newProject.js contains a function that handles the display status (block/none) of the deadline form making it appear when needed otherwise keeping it hidden.
- projectPage.html display the projects information and allow user to add and/or delete tasks and inventory. Allow owner of the project to manage teams, ect.
- projectPage.js handles the javascript for the modals (add tasks, inventory, ect.). To handle the tasks and inventory I use a system similar to redux, where an action is defined using javascript and is submitted to views to handle it in its corresponding way.

## Models:

- **Project model:** database for projects
- **Tasks model:** database for tasks within projects
- **Inventory model:** database for inventory within projects 
- **Room model:** database for discussion rooms for shared projects
Message model: database of all messages within the rooms
- **Relationship model**: In this model, from_user and to_user are foreign keys to the User model, representing the user who initiated the relationship and the user who was added. The status field stores the current status of the relationship, which can be 'pending', 'accepted', or 'rejected'. The created_at field stores the date and time the relationship was created. We also set unique_together = ('from_user', 'to_user') to ensure that each relationship is unique, so that a user cannot send the same request to another user multiple times.



## Asset libraries & Technologies:

Font Awesome SVG Icons library for buttons such as the Edit button.
Google Fonts