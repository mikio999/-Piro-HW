const changeLikeRate = (id, increment) => {
  const likeRateElement = document.getElementById(`like-rate-${id}`);
  const currentRate = parseInt(likeRateElement.innerText);
  const newRate = currentRate + increment;

  const requestLike = new XMLHttpRequest();
  requestLike.open(
    "POST",
    `/pirostagram/change_like_rate/${id}/${newRate}/`,
    true
  );
  requestLike.setRequestHeader("Content-Type", "application/json");

  requestLike.onreadystatechange = () => {
    if (requestLike.readyState === XMLHttpRequest.DONE) {
      if (requestLike.status === 200) {
        const data = JSON.parse(requestLike.responseText);
        likeRateElement.innerText = data.new_rate;
      } else {
        console.error("Error", requestLike.statusText);
      }
    }
  };

  requestLike.send();
};
