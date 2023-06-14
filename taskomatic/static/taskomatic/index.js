    // Element
const editIcons = document.querySelectorAll('.indexEditIcon')
const deleteIcons = document.querySelectorAll('.indexDeleteIcon')
const modal = document.querySelector('.modal');
const closeModal = document.querySelector('.close-modal')
const deleteModalButton = document.querySelector('.delete-modal')
let currentProjectId = ''

    // Event handler
const editFormSubmit = (event) => {
    const currentFormName = event.target.parentElement.id;
    const currentForm = document.getElementById(currentFormName);
    currentForm.submit();
}
const deleteProjectPrompt = (event) => {
    console.log(event.target.id)
    if (event.target.classList.contains('teamProject')) {
        modal.classList.remove('hidden');
        document.querySelector('.modalTitle').innerHTML = 'Remove Project'
        document.querySelector('.modalSubTitle').innerHTML = 'Do you want to permanently exit from this team project?'
        document.querySelector('.delete-modal').innerHTML = 'Exit'
        currentProjectId = event.target.id.replace('indexDeleteIcon', '');
    } else {
        modal.classList.remove('hidden');
        document.querySelector('.modalTitle').innerHTML = 'Delete Project'
        document.querySelector('.modalSubTitle').innerHTML = 'Are you sure?'
        document.querySelector('.delete-modal').innerHTML = 'Delete'
        currentProjectId = event.target.id.replace('indexDeleteIcon', '');
    }
}
const hideModal = () => {
    modal.classList.add('hidden');
}
const submitDeleteRequest = () => {
    const selectDeleteForm = 'toDeleteForm' + currentProjectId;
    form = document.getElementById(selectDeleteForm);
    document.forms[selectDeleteForm].requestSubmit()
}

    // Event listener
for (let i = 0; i < editIcons.length; i++) {
    editIcons[i].addEventListener("click", editFormSubmit);
}
for (let i = 0; i < deleteIcons.length; i++) {
    deleteIcons[i].addEventListener("click", deleteProjectPrompt);
}
closeModal.addEventListener("click", hideModal);
deleteModalButton.addEventListener("click", submitDeleteRequest);