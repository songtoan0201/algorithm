function sudoku2(grid) {
  let N = grid.length;
  let seen = new Set();
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      let cur_val = grid[i][j];
      if (cur_val != ".") {
        if (
          seen.has(cur_val + "found in row" + i) ||
          seen.has(cur_val + "found in column" + j) ||
          seen.has(cur_val + "found in box" + Math.floor(i / 3) + Math.floor(j / 3))
        ) {
          return false;
        } else {
          seen.add(cur_val + "found in row" + i);
          seen.add(cur_val + "found in column" + j);
          seen.add(cur_val + "found in box" + Math.floor(i / 3) + Math.floor(j / 3));
        }
        console.log(seen);
      }
    }
  }
  return true;
}

grid = [
  [".", "4", ".", ".", ".", ".", ".", ".", "."],
  [".", ".", "4", ".", ".", ".", ".", ".", "."],
  [".", ".", ".", "1", ".", ".", "7", ".", "."],
  [".", ".", ".", ".", ".", ".", ".", ".", "."],
  [".", ".", ".", "3", ".", ".", ".", "6", "."],
  [".", ".", ".", ".", ".", "6", ".", "9", "."],
  [".", ".", ".", ".", "1", ".", ".", ".", "."],
  [".", ".", ".", ".", ".", ".", "2", ".", "."],
  [".", ".", ".", "8", ".", ".", ".", ".", "."]
];
console.log(sudoku2(grid));
