    // Toggle variable
let addType

    //Elements
const modal = document.querySelector('.modal');
const modalTitle = document.querySelector('.modalTitle');
const taskModalForm = document.querySelector('.tasksModalForm');
const inventoryModalForm = document.querySelector('.inventoryModalForm');
const addTask = document.querySelector('.addTaskButton');
const taskCompletionCheckboxes = document.querySelectorAll("input[name='taskCompletion']");
const addInventory = document.querySelector('.addInventoryButton');
const closeModal = document.querySelector('.close-modal');
const addModal = document.querySelector('.add-modal');
const editIcon = document.getElementById('editIcon');

    // Event handlers
const showModal = (element) => {
    if (element === 'task') {
        addType = 'task';
        modalTitle.innerHTML = 'Add Task';
        inventoryModalForm.classList.add('hidden');
        taskModalForm.classList.remove('hidden');
        modal.classList.remove('hidden');
    } else {
        addType = 'inventory';
        modalTitle.innerHTML = 'Add Inventory';
        taskModalForm.classList.add('hidden');
        inventoryModalForm.classList.remove('hidden');
        modal.classList.remove('hidden');
    } 
}

const hideModal = () => {
    modal.classList.add('hidden');
}

const editFormSubmit = () => {
    document.editForm.submit();
}

const submitAddForm = (type) => {
    if (type === 'task') {
        document.forms['addTaskForm'].requestSubmit();
    } else if (type === 'inventory'){
        document.forms['addInventoryForm'].requestSubmit();
    }
}

const applyTaskCompletedClass = (checkbox) => {
    console.log('test')
    const currentFormId = checkbox.parentElement.id;
    const currentFormContainer = document.getElementById(`taskInstancesContainer${currentFormId}`);

    if (checkbox.checked) {
        currentFormContainer.classList.add('taskCompleted');
    } else {
        currentFormContainer.classList.remove('taskCompleted');
    }
};

const submitCheckbox = (event) => {
    const currentFormId = event.target.parentElement.id;
    const currentForm = document.getElementById(currentFormId);

    applyTaskCompletedClass(event.target);
    currentForm.requestSubmit();
}

    // Apply initial state of checkboxes
taskCompletionCheckboxes.forEach((checkbox) => {
    applyTaskCompletedClass(checkbox);
});

    // Event listeners
if (addTask){
    addTask.addEventListener("click", () => showModal('task'));
}
if (addInventory) {
    addInventory.addEventListener("click", () => showModal('inventory'));
}

closeModal.addEventListener("click", hideModal);
addModal.addEventListener("click", () => submitAddForm(addType));
editIcon.addEventListener("click", editFormSubmit);
taskCompletionCheckboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", submitCheckbox)
})