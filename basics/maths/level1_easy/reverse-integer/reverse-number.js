/*

problem: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

input: 123 -> output: 321
input: -123 -> output: -321
input: 21474836479 -> output: 0

leetcode: https://leetcode.com/problems/reverse-integer/

*/

/*

Time Complexity: O(log n)
Space Complexity: O(1)

*/
function reverseNumber(input) {
  const sign = input < 0 ? -1 : 1;
  let number = Math.abs(input);
  if (number < 10) return sign * number;
  let reversedNumber = 0;
  const maxRange = 2147483647;
  const minRange = -2147483648;
  while (number) {
    const lastDigit = number % 10;
    number = Math.floor(number / 10);
    reversedNumber *= 10;
    reversedNumber += lastDigit;
  }
  reversedNumber *= sign;
  if (reversedNumber > maxRange || reversedNumber < minRange) return 0;
  return reversedNumber;
}
