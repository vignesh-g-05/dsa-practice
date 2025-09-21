/*

problem: Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

input: [2, 5, 6, 9, 10] -> output: 2
input: [7, 5, 6, 8, 3] -> output: 1
input: [3, 3] -> output: 3

leetcode: https://leetcode.com/problems/find-greatest-common-divisor-of-array

*/

function gcdOfArray(array) {
  let a = array[0];
  let b = array[0];
  for (let i = 1; i < array.length; i++) {
    if (array[i] < a) a = array[i];
    if (array[i] > b) b = array[i];
  }
  if (a === b) return a;
  while (a && b) {
    if (a > b) a = a % b;
    else b = b % a;
  }
  return a || b;
}
