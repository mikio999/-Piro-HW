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

// pireddit.js

const submitComment = (redditId) => {
  const commentText = document.querySelector(
    `#comment-input-${redditId}`
  ).value;

  const requestComment = new XMLHttpRequest();

  requestComment.open("POST", `/pirostagram/submit_comment/${redditId}/`);
  requestComment.setRequestHeader("Content-Type", "application/json");

  requestComment.onload = function () {
    if (requestComment.status === 200) {
      const data = JSON.parse(requestComment.responseText);

      const commentList = document.querySelector(`#comment-list-${redditId}`);
      const newComment = document.createElement("div");
      newComment.classList.add("comment");
      newComment.textContent = data.comment_text;
      commentList.appendChild(newComment);
    } else {
      console.error("Error submitting comment:", requestComment.status);
    }
  };

  requestComment.onerror = function () {
    console.error("Network error occurred.");
  };

  const formData = JSON.stringify({ comment_text: commentText });
  requestComment.send(formData);
};
