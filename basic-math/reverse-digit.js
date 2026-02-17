/*
Leetcode: https://leetcode.com/problems/reverse-integer/

Time Complexity: O(log n)
Space Complexity: O(1)
*/

function solution(n) {
  const maxLimit = Math.pow(2, 31) - 1;
  const minLimit = Math.pow(2, 31) * -1;
  if (n > maxLimit || n < minLimit) return 0;

  let isNegative = false;
  let num = n;
  let rev = 0;
  if (num < 0) {
    num = num * -1;
    isNegative = true;
  }

  while (num > 0) {
    rev *= 10;
    rev += num % 10;
    num = Math.floor(num / 10);
  }

  if (isNegative) {
    rev = rev * -1;
  }
  if (rev > maxLimit || rev < minLimit) return 0;

  return rev;
}
