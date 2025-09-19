/*

problem: Given an integer x, return true if x is a palindrome, and false otherwise.

input: 121 -> output: true
input: -121 -> output: false
input: 10 -> output: flase

leetcode: https://leetcode.com/problems/palindrome-number

*/

/*

Time Complexity: O(log n)
Space Complexity: O(log n)

*/
function stringApproach(input) {
  if (input < 0) return false;
  if (input < 10) return true;
  const inputString = String(input);
  let reversedString = "";
  for (let i = inputString.length - 1; i >= 0; i--)
    reversedString += inputString[i];
  return inputString === reversedString;
}

/*

Time Complexity: O(log n)
Space Complexity: O(1)

*/
function mathApproach(input) {
  if (input < 0) return false;
  if (input < 10) return true;
  let number = input;
  let reversedNumber = 0;
  while (number) {
    const lastDigit = number % 10;
    number = Math.floor(number / 10);
    reversedNumber = reversedNumber * 10 + lastDigit;
  }
  return input === reversedNumber;
}
