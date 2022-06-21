
function toggleChecked(e) {
    const targetClass = 'user_id_' + e.target.className;
    const labelNode = document.querySelectorAll(`label[for=${targetClass}]`)[0];
    labelNode.classList.contains('selected') ? labelNode.classList.remove('selected') : labelNode.classList.add('selected');
} 

const labelNodes = document.querySelectorAll('label')
for(let node of labelNodes) {
    node.addEventListener('mouseup', toggleChecked)
}
