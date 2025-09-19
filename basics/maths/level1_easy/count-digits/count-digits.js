/*

problem: Given an integer N, return the number of digits in N.

input: 7 -> output: 1
input: 12345 -> output: 5

*/

/*

Time Complexity: O(log n)
Space Complexity: O(1)

*/
function bruteForce({ n }) {
  let number = n;
  let count = 0;

  while (number > 1) {
    number /= 10;
    count++;
  }
  return count;
}

/*

Time Complexity: O(1)
Space Complexity: O(1)

*/
function best({ n }) {
  return Math.ceil(Math.log10(n));
}
