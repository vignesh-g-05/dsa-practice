/*

problem: Given two integers N1 and N2, find their greatest common divisor.

input: 9, 12 -> output: 3
input: 10, 5 -> output: 5
input: 7, 7 -> output: 7

*/

/*

Time Complexity: O(min(num1, num2))
Space Complexity: O(1)

*/
function bruteForce([num1, num2]) {
  const smallNumber = Math.min(num1, num2);
  const bigNumber = Math.max(num1, num2);
  if (bigNumber === smallNumber || bigNumber % smallNumber === 0)
    return smallNumber;
  for (let i = smallNumber; i > 0; i--) {
    if (smallNumber % i === 0 && bigNumber % i === 0) return i;
  }
}

/*

Time Complexity: O(log(min(num1, num2)))

*/
function best([num1, num2]) {
  let a = num1;
  let b = num2;

  if (a === b) return a;
  if (Math.max(a, b) % Math.min(a, b) === 0) return Math.min(a, b);

  while (a && b) {
    if (a > b) a = a % b;
    else b = b % a;
  }

  if (a) return a;
  else return b;
}
