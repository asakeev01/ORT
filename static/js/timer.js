const startingMinutes = 30;
let time = startingMinutes * 60;

const countdownEl = document.getElementById('countdown');


setInterval(updateCountDown, 1000);

function updateCountDown() {
    let minutes = Math.floor(time / 60);
    let seconds = time % 60;

    seconds = seconds < 10 ? '0' + seconds : seconds;
    minutes = minutes < 10 ? '0' + minutes : minutes;

    countdownEl.innerHTML = `${minutes}:${seconds}`;
    time--;
    if (time == 0) {
        document.theForm.submit();
    }
}