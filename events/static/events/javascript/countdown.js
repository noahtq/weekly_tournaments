const date = document.currentScript.getAttribute('date');
const countDownElement = document.getElementsByClassName('countdown-text')[0];

function countdown(targetDate) {
    console.log(targetDate);
    const countDownDate = new Date(targetDate).getTime();

    const intervalId = setInterval(() => {
        const now = new Date().getTime();

        const distance = countDownDate - now;

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
        countDownElement.innerHTML = 
        `<div><span class="big">${days}</span><span class="small">Days</span></div>
        <div><span class="big">${hours}</span><span class="small">Hours</span></div>
        <div><span class="big">${minutes}</span><span class="small">Minutes</span></div>
        <div><span class="big">${seconds}</span><span class="small">Seconds</span></div>`

    }, 1000);
}

countdown(date)