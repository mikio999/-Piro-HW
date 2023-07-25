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

const deleteComment = (commentId) => {
  const commentElement = document.getElementById(`comment-${commentId}`);
  if (commentElement) {
    commentElement.remove();
  }

  const request = new XMLHttpRequest();
  request.open("DELETE", `/pirostagram/delete_comment/${commentId}/`);

  request.onload = function () {
    if (request.status !== 200) {
      console.error("댓글 삭제 에러:", request.status);
    }
  };

  request.onerror = function () {
    console.error("네트워크 오류가 발생했습니다.");
  };

  request.send();
};

const submitComment = (redditId) => {
  const commentInput = document.getElementById(`comment-input-${redditId}`);
  if (!commentInput) {
    console.error(`Input element not found for Reddit ID: ${redditId}`);
    return;
  }

  const commentText = commentInput.value;
  console.log(commentText);

  const requestComment = new XMLHttpRequest();

  requestComment.open("POST", `/pirostagram/submit_comment/${redditId}/`);
  requestComment.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );

  requestComment.onload = function () {
    if (requestComment.status === 200) {
      const data = JSON.parse(requestComment.responseText);
      if (data.comment_id) {
        const commentList = document.querySelector(`#comment-list-${redditId}`);
        const newComment = document.createElement("li");
        newComment.classList.add("list-group-item");
        newComment.setAttribute("id", `comment-${data.comment_id}`); // 새 댓글의 ID를 설정합니다.
        newComment.innerHTML = `
          <div>${commentText}</div>
          <span class="delete-comment" onclick="deleteComment(${data.comment_id})">
          <img src="../../static/img/clear.png" style="width:15px;"/>
          </span>
        `;
        commentList.appendChild(newComment);
      } else {
        console.error("Error creating comment: Invalid response data");
      }
    } else {
      console.error("Error submitting comment:", requestComment.status);
    }
  };

  const formData = `comment_text=${encodeURIComponent(commentText)}`;
  requestComment.send(formData);
};
