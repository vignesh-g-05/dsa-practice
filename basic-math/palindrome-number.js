/*
Problem: https://leetcode.com/problems/palindrome-number
*/

/*
Time Complexity: O(log n)
Space Complexity: O(log n)
*/

function solution1(n) {
  if (n < 0) return;
  let num = String(n);
  let rev = "";
  for (let i = 0; i < num.length; i++) {
    rev = num[i] + rev;
  }
  return rev === num;
}

/*
Time Complexity: O(log n)
Space Complexity: O(1)
*/

function solution2(n) {
  if (n < 0) return false;
  if (n < 10) return true;
  if (n % 10 === 0) return false;

  let num = n;
  let rev = 0;

  while (num > 0) {
    rev *= 10;
    rev += num % 10;
    num = Math.floor(num / 10);
  }

  return rev === n;
}
