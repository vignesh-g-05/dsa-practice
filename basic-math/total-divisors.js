/*
input: 36,
expected: [1, 2, 3, 4, 6, 9, 12, 18, 36],
*/

/*
Time Complexity: O(n)
Space Complexity: O(sqrt n)
*/
export function solution1(n) {
  const divisors = [1];
  for (let i = 2; i <= n; i++) {
    if (n % i === 0) {
      divisors.push(i);
    }
  }
  return divisors;
}

/*
Time Complexity: O(n)
Space Complexity: O(sqrt n)
*/
export function solution2(n) {
  const divisors = [1];
  for (let i = 2; i <= n / 2; i++) {
    if (n % i === 0) {
      divisors.push(i);
    }
  }
  divisors.push(n);
  return divisors;
}

/*
Time Complexity: O(sqrt n)
Space Complexity: O(sqrt n)
*/
function solution3(n) {
  const divisors = [1];
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      divisors.push(i);
      if (n / i !== i) divisors.push(n / i);
    }
  }
  divisors.push(n);
  return divisors;
}
