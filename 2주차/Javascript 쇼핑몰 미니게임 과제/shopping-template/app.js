console.log("hello");
// Fetch the items from the JSON file
function loadItems() {
  return fetch(`../shopping-template/data/data.json`)
    .then((response) => response.json())
    .then((json) => console.log(json));
}
console.log(data / data.json);

// main
loadItems()
  .then((items) => {
    console.log(items);
    // displayItems(items);
    // setEventListeners(items);
  })
  .catch(console.log);
