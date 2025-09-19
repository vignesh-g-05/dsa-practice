/*

problem: Given an integer num, return the number of digits in num that divide num.

input: 7 -> output: 1
input: 121 -> output: 2
input: 1248 -> output: 4

leetcode: https://leetcode.com/problems/count-the-digits-that-divide-a-number

*/

/*

Time Complexity: 0(log n)
Space Complexity: 0(1)

*/
function countDigitsDividingNumber(input) {
  let currentNumer = input;
  let totalDivisors = 0;
  while (currentNumer) {
    const divisor = currentNumer % 10;
    currentNumer = Math.floor(currentNumer / 10);
    if (input % divisor === 0) {
      totalDivisors++;
    }
  }
  return totalDivisors;
}
