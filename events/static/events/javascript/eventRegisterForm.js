
//Set current user to selected in registered users update form
function setToSelected() {
    userNodes = document.getElementById('id_registered_users').children;
    const userId = document.currentScript.getAttribute('userId');

    let userOption = undefined
    for(let i = 0; i < userNodes.length; i++) {
        if(userNodes[i].value == userId) {
            userOption = userNodes[i];
        }
    }
    userOption.setAttribute('selected', 'selected')
}


function hideInput() {
    const updateInput = document.getElementById('id_registered_users')
    updateInput.style.display = 'none';

    const updateInputLabel = document.getElementsByTagName('label')[0];
    updateInputLabel.style.display = 'none';
}

setToSelected();
hideInput();

