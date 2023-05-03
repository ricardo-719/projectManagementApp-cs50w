    // Element
const editIcons = document.querySelectorAll('.indexEditIcon')

    // Event handler
const editFormSubmit = (event) => {
    const currentFormName = event.target.parentElement.id;
    const currentForm = document.getElementById(currentFormName);
    currentForm.submit();
}

    // Event listener
for (let i = 0; i < editIcons.length; i++) {
    editIcons[i].addEventListener("click", editFormSubmit);
}
