/*
Time Complexity: O(log n)
Space Complexity: O(1)
*/

export function solution1(n) {
  let num = n;
  let count = 0;
  while (num > 0) {
    num = Math.floor(num / 10);
    count++;
  }
  return count;
}

/*
Time Complexity: O(1)
Space Complexity: O(1)
*/
function solution2(n) {
  return Math.ceil(Math.log10(n));
}
