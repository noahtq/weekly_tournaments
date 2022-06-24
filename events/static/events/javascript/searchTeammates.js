const searchNode = document.getElementById('teammate-searchbar');
const listElements = document.querySelectorAll('li[class=select-item]')

function addBordersToNodes(nodesArray) {

    let iterArray;

    if (!nodesArray) {
        iterArray = listElements;
    } else {
        iterArray = nodesArray;
    }

    if(iterArray.length > 1) {
        //add border to list elements
        for (let i = 0; i < iterArray.length; i++) {
            if(i > 0) {
                try {
                    iterArray[i].style.borderTop = '1px solid var(--base)';
                } catch(error) {
                    return;
                }
            } else {
                iterArray[i].style.borderTop = '';
            }
        }
    } else {
        try {
            for (let listNode of iterArray) {
                listNode.style.borderTop = '';
            }
        } catch(error) {
            return;
        }
    }
}

function updateList(e) {

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
                show = true;
            }
        }
        if (show) {
            visibleNodes.push(listNode);
        }
        show ? listNode.style.display = 'list-item' : listNode.style.display = 'none';
    }

    addBordersToNodes(visibleNodes);

}

searchNode.addEventListener('keydown', updateList);
addBordersToNodes();