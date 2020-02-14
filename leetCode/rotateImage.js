function rotateImage(a) {
  let N = a.length;
  for (let i = 0; i < N; i++) {
    for (let j = i; j < N; j++) {
      let temp = a[j][i];
      a[j][i] = a[i][j];
      a[i][j] = temp;
    }
  }
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N / 2; j++) {
      let temp = a[i][j];
      a[i][j] = a[i][N - 1 - j];
      a[i][N - 1 - j] = temp;
    }
  }
}

a = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];
rotateImage(a);
console.log(a);
