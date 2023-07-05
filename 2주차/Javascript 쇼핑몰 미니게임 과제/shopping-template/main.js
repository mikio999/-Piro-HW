// Fetch the items from the JSON file
const loadItems = () => {
  return fetch("data/data.json")
    .then((response) => response.json())
    .then((json) => console.log(json));
};

// main
loadItems()
  .then((items) => {
    console.log(items);
    // displayItems(items);
    // setEventListeners(items);
  })
  .catch(console.log);
