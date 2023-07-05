document.addEventListener("DOMContentLoaded", () => {
  const timeElement = document.getElementById("time-number");
  const startButton = document.getElementById("start-btn");
  const stopButton = document.getElementById("stop-btn");
  const resetButton = document.getElementById("reset-btn");

  let startTime;
  let timer;

  const formatTime = (time) => {
    let minutes = Math.floor(time / 60000);
    let seconds = Math.floor((time % 60000) / 1000);
    return (
      (minutes < 10 ? "0" : "") +
      minutes +
      ":" +
      (seconds < 10 ? "0" : "") +
      seconds
    );
  };

  const startTimer = () => {
    startTime = Date.now();
    timer = setInterval(updateTimer, 1000);
  };

  const updateTimer = () => {
    let presentTime = Date.now();
    let elapsedTime = presentTime - startTime;
    timeElement.textContent = formatTime(elapsedTime);
  };

  const stopTimer = () => {
    const currentTime = formatTime(Date.now() - startTime);
    createRecord(currentTime);
  };

  const createRecord = (time) => {
    const recordContainer = document.querySelector(".record-box");

    const recordElement = document.createElement("li");
    recordElement.className = "record-time";

    const imageElement = document.createElement("img");
    imageElement.src = "rec.png";
    imageElement.className = "check-btn";
    recordElement.appendChild(imageElement);

    const timeElement = document.createElement("span");
    timeElement.textContent = time;
    recordElement.appendChild(timeElement);

    recordContainer.appendChild(recordElement);
  };

  const resetTimer = () => {
    timeElement.textContent = "00:00";
    clearInterval(timer);
  };

  startButton.addEventListener("click", startTimer);
  stopButton.addEventListener("click", stopTimer);
  resetButton.addEventListener("click", resetTimer);

  const recordContainer = document.querySelector(".record-box");

  recordContainer.addEventListener("click", (event) => {
    if (event.target.classList.contains("check-btn")) {
      const checkBtn = event.target;
      if (checkBtn.classList.contains("changed")) {
        checkBtn.src = "rec.png";
        checkBtn.classList.remove("changed");
      } else {
        checkBtn.src = "button.png";
        checkBtn.classList.add("changed");
      }
    }
  });

  const trashRemove = document.querySelector(".trash-remove");
  trashRemove.addEventListener("click", () => {
    console.log("trash - clicked");
    const recordTimes = document.querySelectorAll(".record-time");
    console.log(recordTimes);
    recordTimes.forEach((recordTime) => {
      const checkBtn = recordTime.querySelector(".check-btn");
      if (checkBtn.src.endsWith("button.png")) {
        recordTime.remove();
      }
    });
  });
});

const checkAll = document.querySelector("#check-all-btn");
checkAll.addEventListener("click", () => {
  const checkBtns = document.querySelectorAll(".check-btn");

  if (checkAll.classList.contains("changed")) {
    checkBtns.forEach((checkBtn) => {
      checkBtn.src = "rec.png";
      checkBtn.classList.remove("changed");
    });
    checkAll.src = "rec.png";
    checkAll.classList.remove("changed");
  } else {
    checkBtns.forEach((checkBtn) => {
      checkBtn.src = "button.png";
      checkBtn.classList.add("changed");
    });
    checkAll.src = "button.png";
    checkAll.classList.add("changed");
  }
});
