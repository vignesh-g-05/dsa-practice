/*

problem: Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.

input: 526 -> output: true
input: 1800 -> output: false
input: 0 -> output: true

*/

/*

Time Complexity: O(log n)
Space Complexity: 0(1)

*/
const reverseNumber = (n) => {
  if (n < 10) return n;
  let number = n;
  let reversedNumber = 0;

  while (number) {
    const lastDigit = number % 10;
    number = Math.floor(number / 10);
    reversedNumber = reversedNumber * 10 + lastDigit;
  }
  return reversedNumber;
};
function numberAfterDoubleReversal(input) {
  return input === reverseNumber(reverseNumber(input));
}
