const searchNode = document.getElementById('teammate-searchbar');
const listElements = document.querySelectorAll('li[class=select-item]')

function updateList(e) {
    for (let listNode of listElements) {
        let show = false;
        childLabel = listNode.children[0];
        grandchildText = childLabel.children;
        for (let grandChild of grandchildText) {
            const innerText = grandChild.innerHTML.toLowerCase()
            if(innerText.includes(e.target.value.toLowerCase())) {
                show = true;
            }
        }
        show ? listNode.style.display = 'list-item' : listNode.style.display = 'none';
    }
}

searchNode.addEventListener('keydown', updateList);