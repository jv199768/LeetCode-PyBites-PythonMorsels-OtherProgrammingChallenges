// Load dictionary (sample) and return as generator (done)
function loadDictionary() {
  const fs = require('fs');
  const dictionary = fs.readFileSync('dictionary_m_words.txt', 'utf8').split('\n');
  return dictionary.map(word => word.toLowerCase().trim());
}

// is_palindrome - checks if a word is a palindrome
function isPalindrome(word) {
  const letters = 'abcdefghijklmnopqrstuvwxyz';
  const abc = letters + letters.toUpperCase();
  const wordCleanup = word.split('').filter(char => abc.includes(char)).join('').toLowerCase();

  const innerPalindrome = (w) => {
    if (w.length <= 0) {
      return true;
    }
    return w[0] === w[w.length - 1];
  };

  return innerPalindrome(wordCleanup);
}

// get_longest_palindrome
function getLongestPalindrome(words = null) {
  if (words === null) {
    words = loadDictionary();
  }

  let currentTop = '';
  for (const word of words) {
    if (isPalindrome(word)) {
      if (word.length > currentTop.length) {
        currentTop = word;
      }
    }
  }

  return currentTop;
}

