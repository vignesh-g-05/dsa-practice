/*

problem: Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

input: 38 -> output: 2
explanation:
     38 --> 3 + 8 --> 11
     11 --> 1 + 1 --> 2
     Since 2 has only one digit, return it.

leetcode: https://leetcode.com/problems/add-digits

*/

/*

Time Complexity: O(log n)
Space Complexity: O(1)

*/
function bruteForce(number) {
  let total = number;
  while (total >= 10) {
    let num = total;
    let sum = 0;
    while (num) {
      const lastDigit = num % 10;
      sum += lastDigit;
      num = Math.floor(num / 10);
    }
    total = sum;
  }
  return total;
}
