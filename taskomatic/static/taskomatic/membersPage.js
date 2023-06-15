    //Element
const toggleMemberBtn = document.querySelectorAll('.toggleMemberBtn')

    //Event handler
const toggleMember = async (event) => {
    const currentFormId = event.target.parentElement.id;
    const parameters = currentFormId.split(" | ");
    const projectId = parameters[1]
    const username = parameters[0]
    const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    const url = `/members/${projectId}`
    
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                "X-CSRFToken": csrfToken,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username })
        });
        if (response.ok) {
            if (event.target.classList.contains('fa-minus')) {
                event.target.outerHTML = '<i class="fa-solid fa-plus cursor-pointer toggleMemberBtn text-sky-600 hover:text-sky-700"></i>'
            } else {
                event.target.outerHTML = '<i class="fa-solid fa-minus cursor-pointer toggleMemberBtn text-red-600 hover:text-red-700"></i>'
            }  
        } else {
            throw new Error('Request failed')
        }
    } catch (error) {
        console.log(error)
    }
}

    //Event listener
toggleMemberBtn.forEach((button) => {
    button.addEventListener("click", toggleMember)
})