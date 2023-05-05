    //Elements
const modal = document.querySelector('.modal');
const modalTitle = document.querySelector('.modalTitle')
const taskModalForm = document.querySelector('.tasksModalForm')
const inventoryModalForm = document.querySelector('.inventoryModalForm')
const addTask = document.querySelector('.addTaskButton');
const addInventory = document.querySelector('.addInventoryButton');
const closeModal = document.querySelector('.close-modal')
const editIcon = document.getElementById('editIcon')

    // Event handlers
const showModal = (element) => {
    if (element === 'task') {
        modalTitle.innerHTML = 'Add Task'
        inventoryModalForm.classList.add('hidden');
        taskModalForm.classList.remove('hidden');
        modal.classList.remove('hidden');
    } else {
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

    // Event listeners
if (addTask){
    addTask.addEventListener("click", () => showModal('task'));
}
if (addInventory) {
    addInventory.addEventListener("click", () => showModal('inventory'));
}
closeModal.addEventListener("click", hideModal);
editIcon.addEventListener("click", editFormSubmit);