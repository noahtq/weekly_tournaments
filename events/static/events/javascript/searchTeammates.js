const searchNode = document.getElementById('teammate-searchbar');
const listElements = document.querySelectorAll('li[class=select-item]')

function updateList(e) {

    //add border to list elements
    for (let i = 0; i < listElements.length; i++) {
        if(i > 1) {
            listElements[i].style.borderTop = '1px solid var(--base)';
        }
    }

    if(e.target.value.trim() == '') {
        for (let listNode of listElements) {
            listNode.style.display = 'list-item';
        }
    }

    const visibleNodes = [];

    for (let listNode of listElements) {
        let show = false;
        childLabel = listNode.children[0];
        grandchildText = childLabel.children;
        for (let grandChild of grandchildText) {
            const innerText = grandChild.innerHTML.toLowerCase()
            if(innerText.includes(e.target.value.toLowerCase())) {
                visibleNodes.push(listNode);
                show = true;
            }
        }
        show ? listNode.style.display = 'list-item' : listNode.style.display = 'none';
    }

    //remove border if there is only one list element visible
    if (visibleNodes.length <= 2) {
        for (let listNode of listElements) {
            listNode.style.borderTop = '0px solid black';
        }
    }
}

searchNode.addEventListener('keydown', updateList);