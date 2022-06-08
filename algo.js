function bubbleSort(arr) {
  for (var i = 0; i < arr.length; i++) {
    for (var j = i; j < arr.length; j++) {
      if (arr[j] > arr[j + 1]) {
        var temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
}

console.log(
  bubbleSort([
    2, 1, 6, 9, 5, 3, 4, 1, 2, 2, 1, 6, 9, 5, 3, 4, 1, 2, 2, 1, 6, 9, 5, 3, 4,
    1, 2, 0, 2, 1, 6, 9, 5, 3, 4, 1, 2,
  ])
);
