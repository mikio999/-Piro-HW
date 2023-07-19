function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function changeInterestRate(ideaId, increment) {
  const interestRateElement = document.getElementById(
    `interest-rate-${ideaId}`
  );
  const currentRate = parseInt(interestRateElement.innerText);
  const newRate = currentRate + increment;

  fetch(`/change_interest_rate/${ideaId}/${newRate}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
  })
    .then((response) => response.json())
    .then((data) => {
      interestRateElement.innerText = data.new_rate;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
