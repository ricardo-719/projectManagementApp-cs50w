# Task-o-Matic

A web-app for project management where the user is able to keep track of things such as deadlines, tasks and inventories. The application will alert according to user specifications and different views will provide overall information about one or more projects. Teams can be created with shared information, with the option of setting a Project Manager to follow-up on each of the team members, suggests tasks and set deadlines, etc.

Files:

- index.html...
- views.py...
- models.py...
- newProject.html...
- newProject.js contains a function that handles the display status (block/none) of the deadline form making it appear when needed otherwise keeping it hidden.
- projectPage.html display the projects information and allow user to add and/or delete tasks and inventory. Allow owner of the project to manage teams, ect.
- projectPage.js handles the javascript for the modals (add tasks, inventory, ect.)

Models:

Project model: database for projects
Tasks model : database for tasks within projects
Inventory model: database for inventory within projects 
Room model: database for discussion rooms for shared projects
Message model: database of all messages within the rooms