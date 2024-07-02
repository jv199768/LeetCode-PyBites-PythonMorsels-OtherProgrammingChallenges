function reverseOnlyLetters(input) {
  let ans = Array.from(input);
  let i = 0;
  let j = ans.length - 1;

  while (i < j) {
    while (i < j && !/[a-zA-Z]/.test(ans[i])) {
      i++;
    }
    while (i < j && !/[a-zA-Z]/.test(ans[j])) {
      j--;
    }
    [ans[i], ans[j]] = [ans[j], ans[i]];
    i++;
    j--;
  }

  return ans.join('');
}

