/*
Time Complexity: O(min(num1, num2))
Space Complexity: O(1)
*/

function solution1([num1, num2]) {
  if (num1 === num2) return num1;
  let gcd = 1;
  for (let i = 2; i <= Math.min(num1, num2); i++) {
    if (num1 % i === 0 && num2 % i === 0) gcd = i;
  }
  return gcd;
}

/*
Time Complexity: O(min(num1, num2))
Space Complexity: O(1)
*/

function solution2([num1, num2]) {
  for (let i = Math.min(num1, num2); i > 1; i--) {
    if (num1 % i === 0 && num2 % i === 0) return i;
  }
}

/*
Time Complexity: O(max(num1, num2))
Space Complexity: O(1)
*/

function solution3([num1, num2]) {
  let a = num1;
  let b = num2;

  while (a !== 0 && b !== 0) {
    if (a > b) {
      a = a - b;
    } else {
      b = b - a;
    }
  }

  return a || b;
}
