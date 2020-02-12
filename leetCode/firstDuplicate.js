function firstDuplicate(a) {
  let check = {};
  for (let i = 0; i < a.length; i++) {
    if (!check.hasOwnProperty(a[i])) {
      check[a[i]] = i;
    } else {
      return a[i];
    }
    console.log("dict", check);
  }
  return -1;
}

console.log(firstDuplicate([2, 1, 3, 5, 3, 2]));
