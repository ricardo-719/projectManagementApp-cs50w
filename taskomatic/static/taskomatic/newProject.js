let element = document.getElementById('projectDeadlineCheckbox');
let deadlineDateInput = document.getElementById('containerDeadlineDate');

element.addEventListener("change", () => {
    if (element.checked) {
        deadlineDateInput.style.visibility = 'visible';
        deadlineDateInput.style.opacity = '1';
    } else {
        deadlineDateInput.style.visibility = 'hidden';
        deadlineDateInput.style.opacity = '0';
    }
})