/*

problem: You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:

input: 4 => output: 4
explaination:
Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16
Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20
Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.

leetcode: https://leetcode.com/problems/gcd-of-odd-and-even-sums/

*/

/*

Time Complexity: O(min(a,b))
Space Complexity: O(1)

*/
function bruteForce(number) {
  let a = number * number; // sum of n odd numbers
  let b = number * (number + 1); // sum of n even numbers
  while (a && b) {
    if (a > b) {
      a %= b;
    } else {
      b %= a;
    }
  }
  return a || b;
}

/*

Time Complexity: 0(1)
Space Complexity: O(1)

*/
var best = function (number) {
  return number;
};
