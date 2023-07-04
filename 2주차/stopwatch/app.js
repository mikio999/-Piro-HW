const timeElement = document.getElementById("time-number");
const startButton = document.getElementById("start-btn");
const stopButton = document.getElementById("stop-btn");
const resetButton = document.getElementById("reset-btn");

let startTime;
let timer;

function formatTime(time) {
  let minutes = Math.floor(time / 60000);
  let seconds = Math.floor((time % 60000) / 1000);
  return (
    (minutes < 10 ? "0" : "") +
    minutes +
    ":" +
    (seconds < 10 ? "0" : "") +
    seconds
  );
}

function startTimer() {
  startTime = Date.now();
  timer = setInterval(updateTimer, 1000);
  console.log(startTime);
}

function updateTimer() {
  let presentTime = Date.now();
  let elapsedTime = presentTime - startTime;
  timeElement.textContent = formatTime(elapsedTime);
}

function stopTimer() {
  const currentTime = formatTime(Date.now() - startTime);
  createRecord(currentTime);
}

function createRecord(time) {
  const recordContainer = document.querySelector(".record-box");

  const recordElement = document.createElement("div");
  recordElement.className = "record-time";

  const imageElement = document.createElement("img");
  imageElement.src = "rec.png";
  imageElement.className = "check-btn";
  recordElement.appendChild(imageElement);

  const timeElement = document.createElement("span");
  timeElement.textContent = time;
  recordElement.appendChild(timeElement);

  recordContainer.appendChild(recordElement);
}

function resetTimer() {
  timeElement.textContent = "00:00";
  clearInterval(timer);
}

startButton.addEventListener("click", startTimer);
stopButton.addEventListener("click", stopTimer);
resetButton.addEventListener("click", resetTimer);

const checkBtn = document.querySelector(".check-btn");
let isChanged = false;

checkBtn.addEventListener("click", () => {
  if (isChanged) {
    checkBtn.src = "rec.png";
    isChanged = false;
  } else {
    checkBtn.src = "button.png";
    isChanged = true;
  }
});
