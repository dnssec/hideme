- Find an element
    ```js
    let items = [{name: 'sbr', age: 28}, {name: 'sumaiya', age: 22}, {name: 'raiyan', age: 1.5}];
    // Returns the value of the first element in the array where predicate is true,
    // and undefined otherwise
    items.find((item) => item.name === 'raiyan');
    // returns {name: 'raiyan', age: 1.5}  
    ```
- Find an element index
    ```js
    let items = [{name: 'sbr', age: 28}, {name: 'sumaiya', age: 22}, {name: 'raiyan', age: 1.5}];
    // Returns the value of the first element in the array where predicate is true
    // and -1 otherwise
    items.findIndex((item) => item.name === 'sumaiya');
    // returns 1  
    ```
- Filter elements
```js
    let items = [{name: 'sbr', age: 28}, {name: 'sumaiya', age: 22}, {name: 'raiyan', age: 1.5}];
    // Returns the elements of an array that meet the condition specified in a callback function, 
    // and empty array otherwise
    items.filter((item) => item.name.startsWith('s'));
    // returns [{name: 'sbr', age: 28}, {name: 'sumaiya', age: 22}]
```
