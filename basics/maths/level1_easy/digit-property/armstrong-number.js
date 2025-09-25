/*

problem: Given an integer N, return true it is an Armstrong number otherwise return false.
An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

input: 153 -> output: true
explaination: 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

*/

/*

Time Complexity: O(log n)
Space Complexity:O(1)
*/
function solution1(number) {
  if (number < 10) return true;
  let totalDigits = 0;
  let num = number;
  let sum = 0;
  while (num) {
    num = Math.floor(num / 10);
    totalDigits++;
  }
  num = number;
  while (num) {
    const extractedDigit = num % 10;
    sum += Math.pow(extractedDigit, totalDigits);
    num = Math.floor(num / 10);
  }
  return sum === number;
}

function solution2(number) {
  if (number < 10) return true;
  let totalDigits = String(number).length;
  let num = number;
  let sum = 0;
  while (num) {
    const extractedDigit = num % 10;
    sum += Math.pow(extractedDigit, totalDigits);
    num = Math.floor(num / 10);
  }
  return sum === number;
}
