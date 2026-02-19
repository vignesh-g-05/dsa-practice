/*
Time Complexity: O(log n)
Space Complexity: O(1)
*/

function solution1(n) {
  if (n < 10) return true;
  const power = String(n).length;
  let num = n;
  let res = 0;
  while (num > 0) {
    const last = num % 10;
    res += last ** power;
    num = Math.floor(num / 10);
  }
  return res === n;
}
