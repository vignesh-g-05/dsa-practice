/*
Time Complexity: O(n)
Space Complexity: O(1)
*/

function solution({ arr }) {
  let max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }
  return max;
}
