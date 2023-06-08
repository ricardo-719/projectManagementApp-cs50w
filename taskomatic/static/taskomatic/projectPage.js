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
    //Inventory restock & consument buttons
const incrementButtons = document.querySelectorAll('.increment-btn');
const decrementButtons = document.querySelectorAll('.decrement-btn');
const inventoryEditBtns = document.querySelectorAll('.inventoryEditBtns')

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

    // Restock & Consume inventory event listeners
incrementButtons.forEach((button) => {
    button.addEventListener('click', async (e) => {
        e.preventDefault();
        const pk = e.target.dataset.pk;
        const url = `/handleInventory/increment/${pk}`;
        const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    "X-CSRFToken": csrfToken
                },
                body: JSON.stringify({})
            });
            if(response.ok) {
                const qtyInstance = document.getElementById(`qty${pk}`);
                const currentQty = parseInt(qtyInstance.innerText)
                qtyInstance.innerText = currentQty + 1;
            } else {
                throw new Error('Request failed')
            }
        } catch (error) {
            console.log(error)
        }
    });
});

decrementButtons.forEach((button) => {
    button.addEventListener('click', async (e) => {
        e.preventDefault();
        const pk = e.target.dataset.pk;
        const url = `/handleInventory/decrement/${pk}`;
        const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    "X-CSRFToken": csrfToken
                },
                body: JSON.stringify({})
            });
            if(response.ok) {
                const qtyInstance = document.getElementById(`qty${pk}`);
                const currentQty = parseInt(qtyInstance.innerText)
                qtyInstance.innerText = currentQty - 1;
            } else {
                throw new Error('Request failed')
            }
        } catch (error) {
            console.log(error)
        }
    });
});

inventoryEditBtns.forEach((button) => {
    button.addEventListener('click', async (e) => {
        e.preventDefault();
        const pk = e.target.dataset.pk;
        const url = `/handleInventory/edit/${pk}`;
        const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    "X-CSRFToken": csrfToken
                },
                body: JSON.stringify({})
            });
            if (response.ok) {
                const data = await response.json();
                const inventoryPageHtml = data.inventoryPage_html
                document.getElementById('addInventoryForm').outerHTML = inventoryPageHtml
                showModal('inventory')
            } else {
                throw new Error('Request failed')
            }
        } catch (error) {
            console.log(error)
        }
    });
});