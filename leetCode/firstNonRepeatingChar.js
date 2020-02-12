function firstNotRepeatingCharacter(s) {
  check = {};
  for (let i = 0; i < s.length; i++) {
    if (!check.hasOwnProperty(s[i])) {
      check[s[i]] = 1;
    } else {
      check[s[i]] += 1;
    }
    console.log(check);
  }
  for (let i = 0; i < s.length; i++) {
    if (check[s[i]] == 1) {
      return s[i];
    }
  }
  return "_";
}

console.log(firstNotRepeatingCharacter("abacabaabaabac"));
