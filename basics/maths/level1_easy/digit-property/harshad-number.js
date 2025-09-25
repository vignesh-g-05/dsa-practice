/*

problem: An integer divisible by the sum of its digits is said to be a Harshad number. You are given an integer x. Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.

input: 18 -> output: 9
explaination: The sum of digits of x is 9. 18 is divisible by 9. So 18 is a Harshad number and the answer is 9.

leetcode: https://leetcode.com/problems/harshad-number

*/

/*

Time Complexity: O(log n)
Space Complexity: O(1)
*/
function harshadNumber(number) {
  if (number < 10) return number;
  let num = number;
  let sum = 0;
  while (num) {
    const extractedDigit = num % 10;
    sum += extractedDigit;
    num = Math.floor(num / 10);
  }
  return number % sum ? -1 : sum;
}
