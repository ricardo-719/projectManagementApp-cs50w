    // Toggle variable
let addType

    //Elements
const modal = document.querySelector('.modal');
const modalTitle = document.querySelector('.modalTitle')
const taskModalForm = document.querySelector('.tasksModalForm')
const inventoryModalForm = document.querySelector('.inventoryModalForm')
const addTask = document.querySelector('.addTaskButton');
const addInventory = document.querySelector('.addInventoryButton');
const closeModal = document.querySelector('.close-modal');
const addModal = document.querySelector('.add-modal');
const editIcon = document.getElementById('editIcon');

    // Event handlers
const showModal = (element) => {
    if (element === 'task') {
        addType = 'task';
        console.log(addType)
        modalTitle.innerHTML = 'Add Task';
        inventoryModalForm.classList.add('hidden');
        taskModalForm.classList.remove('hidden');
        modal.classList.remove('hidden');
    } else {
        addType = 'inventory';
        console.log(addType);
        modalTitle.innerHTML = 'Add Inventory'
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
    console.log('function')
    if (type === 'task') {
        document.forms['addTaskForm'].requestSubmit()
    } else if (type === 'inventory'){
        document.forms['addInventoryForm'].requestSubmit()
    }
}

    // Event listeners
if (addTask){
    addTask.addEventListener("click", () => showModal('task'));
}
if (addInventory) {
    addInventory.addEventListener("click", () => showModal('inventory'));
}
console.log(addType)
closeModal.addEventListener("click", hideModal);
addModal.addEventListener("click", () => submitAddForm(addType));
editIcon.addEventListener("click", editFormSubmit);