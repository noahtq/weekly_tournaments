
function toggleChecked(e) {
    const targetClass = 'user_id_' + e.target.className;
    console.log(targetClass);
    const labelNode = document.querySelectorAll(`label[for=${targetClass}]`)[0];
    console.log(labelNode);
    labelNode.classList.contains('selected') ? labelNode.classList.remove('selected') : labelNode.classList.add('selected');
} 

const labelNodes = document.querySelectorAll('label')
for(let node of labelNodes) {
    node.addEventListener('mouseup', toggleChecked)
}
