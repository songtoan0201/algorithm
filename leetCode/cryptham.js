function isCryptSolution(crypt, solution) {
  let word1 = "";
  let word2 = "";
  let word3 = "";
  for (let i = 0; i < crypt[0].length; i++) {
    for (let j = 0; j < solution.length; j++) {
      if (solution[j][0] == crypt[0][i]) {
        word1 += solution[j][1];
      }
    }
  }

  for (let i = 0; i < crypt[1].length; i++) {
    for (let j = 0; j < solution.length; j++) {
      if (solution[j][0] == crypt[1][i]) {
        word2 += solution[j][1];
      }
    }
  }
  for (let i = 0; i < crypt[2].length; i++) {
    for (let j = 0; j < solution.length; j++) {
      if (solution[j][0] == crypt[2][i]) {
        word3 += solution[j][1];
      }
    }
  }
  console.log(word1);
  console.log(word2);
  console.log(word3);
  if (
    word1[0] != "0" &&
    word2[0] != "0" &&
    word3[0] != "0" &&
    parseInt(word1) + parseInt(word2) == parseInt(word3)
  )
    return true;
  else if (
    word1[0] == "0" &&
    word2[0] == "0" &&
    word3[0] == "0" &&
    word1.length == 1 &&
    word3.length == 1 &&
    word2.length == 1
  )
    return true;
  return false;
}
solution = [
  ["O", "1"],
  ["T", "0"],
  ["W", "9"],
  ["E", "5"],
  ["N", "4"]
];
crypt = ["TEN", "TWO", "ONE"];
console.log(isCryptSolution(crypt, solution));
