// Fetch the items from the JSON file
function loadItems() {
  return fetch(`data/data.json`)
    .then((response) => response.json())
    .then((json) => json.items);
}

//Update the list with the given items

const displayItems = (items) => {
  const container = document.querySelector(".items");
  // const html = items.map((item) => createHTMLString(item)).join("");
  // console.log(html);
  container.innerHTML = items.map((item) => createHTMLString(item)).join("");
};

//Create HTML list item from the given data item

const createHTMLString = (item) => {
  return `
  <li class="item">
    <img src="${item.image}" alt="${item.type}" class="item_thumbnail" />
    <span class="item__description">${item.gender}, ${item.size}</span>
  </li>
  `;
};

const onButtonClick = (event, items) => {
  const dataset = event.target.dataset;
  const key = dataset.key;
  const value = dataset.value;

  if (key == null || value == null) {
    return;
  }

  // updateItems(items, key, value);
  filtered = items.filter((item) => item[key] === value);
  // console.log(filtered);
  displayItems(filtered);
};

// function updateItems(items, key, value) {
//   items.forEach((item) => {
//     const dataset = item.dataset;
//     if (dataset[key] === value) {
//       item.classList.remove("invisible");
//     } else {
//       item.classList.add("invisible");
//     }
//   });
// }

const setEventListeners = (items) => {
  const logo = document.querySelector(".logo");
  const buttons = document.querySelector(".buttons");
  logo.addEventListener("click", () => displayItems(items));
  buttons.addEventListener("click", (event) => onButtonClick(event, items));
};

// main
loadItems()
  .then((items) => {
    displayItems(items);
    setEventListeners(items);
  })
  .catch(console.log);
