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

- views.py...
    edit_project: Takes the project's id as an argument and pre-fill forms for editing the project.
    delete_project: Takes the project's id through a POST request and updates the database by deleting the corresponding project.

- forms.py : this file contains all ModelForms of the project. The purpose is to have a better organized project by separation of concerns and in this way not having to rely on the views.py the manage things related to the forms. 

### Models:

- **User model:** extends the built-in Django AbstractUser model, providing additional fields and methods. It allows to store information about users of the application.
- **Project model:**  represents a project. It includes fields such as user, owner, projectName, projectDescription, hasDeadline, hasInventory, hasTasks, creationDate, and deadlineDate. It allows to store information about projects created by users, set deadlines and provide information in terms of visualization of tasks and inventory.
- **Tasks model:** represents a task for a given project. It includes fields such as projectId, taskCreator, taskName, taskDescription, taskDeadline, taskImportance, taskLimitAlert, and taskCreationDate. It allows you to store information about tasks for a given project.
- **Inventory model:** represents an inventory of items for a given project. It includes fields such as projectId, itemName, itemDescription, itemQty, itemUnit, and itemLimitAlert. It allows you to store information about items in an inventory for a given project.
- **Room model:** database for discussion rooms for shared projects
Message model: database of all messages within the rooms
- **Relationship model**: In this model, from_user and to_user are foreign keys to the User model, representing the user who initiated the relationship and the user who was added. The status field stores the current status of the relationship, which can be 'pending', 'accepted', or 'rejected'. The created_at field stores the date and time the relationship was created. We also set unique_together = ('from_user', 'to_user') to ensure that each relationship is unique, so that a user cannot send the same request to another user multiple times.



## Asset libraries & Technologies:

Font Awesome SVG Icons library for buttons such as the Edit button.
Google Fonts


<!-- - projectPage.js handles the javascript for the modals (add tasks, inventory, ect.). To handle the tasks and inventory I use a system similar to redux, where an action is defined using javascript and is submitted to views to handle it in its corresponding way. -->