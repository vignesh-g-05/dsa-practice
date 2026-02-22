/*
Problem: Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.

input: 2
output: true
*/

/*
Time Complexity: O(n)
Space Complexity: O(1)
*/

function solution1(n) {
  if (n < 4) return true;
  if (n % 2 === 0) return false;
  let isPrime = true;
  for (let i = 3; i < n; i++) {
    if (n % i === 0) {
      isPrime = false;
      break;
    }
  }
  return isPrime;
}

/*
Time Complexity: O(sqrt n)
Space Complexity: O(1)
*/

function solution2(n) {
  if (n < 4) return true;
  if (n % 2 === 0) return false;
  let isPrime = true;
  for (let i = 3; i * i <= n; i++) {
    if (n % i === 0) {
      isPrime = false;
      break;
    }
  }
  return isPrime;
}
