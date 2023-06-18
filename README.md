# Task-o-Matic

A web-app for project management where the user is able to keep track of things such as deadlines, tasks and inventories. This intuitive platform not only facilitates individual project organization but also enables seamless team collaboration. Users can form teams within the application, fostering effective communication and cooperation throughout the project lifecycle. The app incorporates a comment system, allowing team members to engage in discussions and provide feedback. Effortlessly stay on top of deadlines, manage tasks, and maintain inventories with Task-O-Matic.

The application will alert and notify the user based on its configuration, and different views will provide overall information about one or more projects. Teams can be created with shared information, with the option of setting a Project Manager to follow-up on each of the team members, suggests tasks, set deadlines, create and manage inventory, invite and manage members, comment and discuss, and much more. 

## Distinctiveness and Complexity

This project implement CRUD operations to enable a wide range of functionalities. Although it possesses a simple core structure, it effectively addresses real-life problems through ingenious solutions. The project contains files that interact in a effective way, improving the performance of the project, for instance, some of the server-side functions employ a Redux-like approach, categorizing operations into actions and ensuring appropriate outcomes for each action. This thoughtful design choice promotes code comprehension, fosters organization, and significantly enhances code readability. By leveraging these principles, the project delivers robust functionality while maintaining a clean and well-structured codebase.

## Files

### Static:

- **styles.css:** This file requires no introduction. It contains styling for many elements across the web application. In addition to this file, TailwindCSS is also used for styling, this framework helps simplifying the process of styling, allowing the code to be more understandable. styles.css is used to define the styling of general and important components of the web application, TailwindCSS helps fine tuning at a smaller scale.

- **index.js, newProject.js, membersPage.js & projectPage.js:** These files play crucial roles in their respective pages by enabling event listeners and handlers, as well as implementing AJAX functionality for specific operations.

    Some notable examples of operations managed by these files include:

    - ***Toggle of modals:*** The files handle the display and hiding of modals based on user actions, providing a dynamic and interactive interface.

    - ***CRUD operations:*** Each file facilitates Create, Read, Update, and Delete operations, allowing users to interact with and manipulate data specific to their respective pages.

    - ***Asynchronous calls:*** The files manage asynchronous requests, enabling the retrieval or submission of data without interrupting the overall browsing experience.

### Templates:

- **index.html:**  The index.html file serves as the landing page of the project, setting the initial impression for users. It contains two different views: one for unauthenticated users and another for authenticated users. 

    The **unauthenticated** user view is designed to be visually appealing and features a clear call-to-action, enabling users to easily start using the app by either logging in or registering.

    For **authenticated** users, the main dashboard is immediately presented. The main dashboard contains a **Contact section** where users have access to their contacts, it also contains a **Notification section** where users are able to see all their alerts and notifications. And finally, in contain all on-going projects of the user. The ongoing projects are divided in personal projects and team projects. On this page the user can easily review all of their projects with their basic information, but also they can edit, remove and delete projects. Before any permanent action is performed, a confirmation modal helps to prevent potential mistakes by the user.

    The **index.html** work together with **index.js** and **styles.css** files to deliver a cohesive and engaging user experience.

- **newProject.html:** This file is a page that allow users to create a new project within their account. It provides a user-friendly form where users can input essential information about their project. This page can be accessed through the navigation menu by clicking on a link labeled "New Project."

    The form in newProject.html includes several fields to capture pertinent project details. These fields allow users to input the following information:

    - ***Project title:*** Users can provide a concise and descriptive title for their project.

    - ***Project description:*** This field enables users to provide a detailed description of their project, outlining its purpose, goals, or any other relevant information.

    - ***Tasks:*** Users can choose to enable the use of tasks for their project by toggling a checkbox. This feature allows for effective task management and tracking within the project.

    - ***Inventory:*** Similar to tasks, users have the option to enable the use of inventory by toggling a checkbox. This functionality facilitates efficient management of project resources and materials.

    - ***Deadline:*** Users can set a deadline for their project by specifying the desired date and time.

    Upon completing the form, users can submit the project details by clicking a designated button. The form utilizes Django Forms, leveraging Django's robust system for form handling, cleaning, and prepopulation. This integration enhances the user experience by ensuring data integrity and simplifying the process of editing or updating project information.

- **projectPage.html:** This file serves as a comprehensive hub for all project-related information and activities. It encompasses four notable sections, each contributing to the management and collaboration within the project.

    1. ***Description Section:*** This section displays a brief description of the project. This allow users to capture and reference important goals, values, vision, or objectives. It serves as a reminder and a central location to maintain crucial project details.

    2. ***Tasks Section:*** In this section,  users can add and manage tasks relevant to the project. It features a button that opens a modal with a form where users can input task information, such as task description, importance value, deadline, and time-sensitive alerts. Completed tasks are sorted in the lower part of the section, visually distinguished with a grayed-out and crossed-out appearance. 

    3. ***Inventory Section:*** This section centralizes all inventory items associated with the project. It provides a comprehensive view of the current inventory status. Users can utilize the "Add inventory" button to input inventory items and define restock limits. Each inventory item instance offers convenient Consume and Restock buttons to increment or decrease quantities by one. Users can also easily edit item instances and update quantities. When an item reaches the restock level defined by the user, it is sorted in the lower part "To be restocked" section, notifying the user that restocking is required.

    4. ***Comment/Discussion Section:*** This section serves as a platform for discussion, remarks, and collaboration. For team projects, it facilitates effective communication among team members. Even for individual projects, this section can be utilized as a journal, reminder, or notes section for the user.

    The project page has been designed and tested for responsiveness, improving user experience across various devices, including mobile devices. 
    
    From the project page, users can edit project information

    The project page is closely associated with the member's page. Together, these pages enable users to add members to projects. When a member is added to a project, they receive a notification and gain access to the project from their own dashboard. Additionally, users can also edit project information from the project page

- **membersPage.html:** This file allow users can see their contact list and easily invite them to the current project. This page is accessible from their respective project page, so the invitation is only for the associated project.

-   **users.html:** This file is associated with the Search functionality. When an user uses the search bar this page displays all partial and exact matches for the query. This page contains to sections: All Users, and My Contacts. This way simultaniously seach for all matches on the general dabase and all matches wihin the user's contact list.

- **layout.html:** Layout serves as a fundamental component in creating a consistent and user-friendly web application.  It includes essential elements such as the header, search bar, and navigation, which are utilized across multiple templates within the project. 

    This file plays a important role in creating a WebApp that is consistent across its different pages and that its easy to navigate.

- **login.html and register.html:**: These two files feature simple yet effective forms that facilitate the login and registration processes for users, respectively.

    Both files prioritize simplicity and ease of use, enabling users to quickly and efficiently complete the login and registration processes.

- **inventoryForm.html:** This file is a utility file that contains the propopulated version of the inventory form. This is injected to the project page with certain customizations. This solution was created due to certain limitations in prepopulating a hidden modal.

### Forms (forms.py): 

The **forms.py** file within the project serves as a centralized location for all ModelForms. Its purpose is to promote better organization and separation of concerns within the project, ensuring that form-related functionality is decoupled from the views.py file.

Some of the ModelForms used and their configurations, are as follow:

- **ProjectForm:** This ModelForm is associated with the **Project** model. It includes fields for all the attributes of the Project model and utilizes various widgets to customize the appearance and behavior of the form inputs. For example, it uses TextInput and Textarea widgets for text-based inputs, CheckboxInput for checkbox inputs, and DateInput for date inputs. These widgets are equipped with attributes such as CSS classes, placeholders, and specific IDs to enhance the user experience.

- **TaskForm:** This ModelForm corresponds to the **Tasks** model. Similar to the ProjectForm, it utilizes different widgets to customize the form inputs. The form includes hidden inputs (HiddenInput) for the projectId and taskCreator fields. Other fields such as taskName, taskDescription, taskDeadline, and taskLimitAlert are configured with appropriate widgets like TextInput, Textarea, and DateInput.

- **CompletionTaskForm:** This ModelForm is related with the tasks model but it serves the specific purpose of updating the Complete state of tasks. The reason why I separated this form from the TaskForm is because I wanted to isolate the process for data cleaning. It includes a single field, taskCompletion, which is a checkbox input (CheckboxInput). The form is designed to take a task_id parameter, which allows for the prepopulation of the checkbox input with the given task ID.

- **InventoryForm:** This ModelForm is associated with the **Inventory** model. It includes fields for all the attributes of the Inventory model. The form utilizes different widgets, such as TextInput, Textarea, and NumberInput, to handle inputs for the item name, item description, item quantity, and restock limit.

- **CommentForm:** This ModelForm corresponds to the **Comment** model and includes a single field, comment. The form is configured with a Textarea widget to accommodate multiline comments.

By defining these ModelForms within the forms.py file, the project achieves a more organized and modular approach to form handling. The separation of concerns allows for easy customization and management of form-related operations, promoting code reusability and maintainability.

### Models (models.py):

- **User model:** This model extends the built-in Django AbstractUser model, which provides basic user fields. The User model does not add any additional fields or methods beyond what is provided by AbstractUser.

- **Project model:**  This model represents a project in the application. It includes fields such as user, owner, projectName, projectDescription, hasDeadline, hasInventory, hasTasks, creationDate, and deadlineDate. The Project model allows storing information about projects created by users, including details like project name, description, deadlines, and whether it has tasks or an inventory associated with it.

- **Member model:** This model associates a project with a user. It uses foreign keys to establish a relationship between the Project model and the User model. The Member model allows providing access permission to relevant users. Users associated with a particular project become members and gain access to the project.

- **Inventory model:** This model represents an inventory of items for a given project. It includes fields such as projectId, itemName, itemDescription, itemQty, itemUnit, and itemLimitAlert. The Inventory model allows storing information about items in an inventory for a specific project, including their names, descriptions, quantities, units, and restock alerts.

- **Tasks model:** This model represents a task for a given project. It includes fields such as projectId, taskCreator, taskName, taskDescription, taskCompletion, taskDeadline, taskImportance, taskLimitAlert, and taskCreationDate. The Tasks model allows storing information about tasks associated with a particular project. It includes details like task name, description, completion status, deadlines, importance, and task creation date.

- **Room & Message model:** These models purpose if for enabling discussion rooms for shared projects with its respective database for all messages within the rooms. *(This model has been defined but not implemented. The implementation of the rooms/messages will be completed on a later version of this project.)*

- **Relationship model**: In this model, from_user and to_user are foreign keys to the User model, representing the user who initiated the relationship and the user who was added. The status field stores the current status of the relationship, which can be 'pending', 'accepted', or 'rejected'. The created_at field stores the date and time the relationship was created. I also set unique_together = ('from_user', 'to_user') to ensure that each relationship is unique, so that a user cannot send the same request to another user multiple times.

- **Notification model:** This model allows for the association of a user with particular notifications. These render in the notification section and can easily be dismissed by the users. While most notifications are contained in this database, this is not the only way the notification section (in the index page) is populated. For instance, the notification section uses the relationship database for the handling of contact request. 

- **Comment model:** The comment model is a simple model for the comment section in each project. For this reason I used a Foreign key to each project and register relevant data for each comment such as, content, date, time & user.

### Views (views.py):

    edit_project: Takes the project's id as an argument and pre-fill forms for editing the project.
    delete_project: Takes the project's id through a POST request and updates the database by deleting the corresponding project. -->

## Asset libraries & Technologies:

Font Awesome SVG Icons library for buttons such as the Edit button.
Google Fonts

<!-- - projectPage.js handles the javascript for the modals (add tasks, inventory, ect.). To handle the tasks and inventory I use a system similar to redux, where an action is defined using javascript and is submitted to views to handle it in its corresponding way. -->