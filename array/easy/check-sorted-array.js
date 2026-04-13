/*
Time Complexity: O(n)
Space Complexity: O(1)
*/

function solution({ arr }) {
  if (arr.length < 2) return true;
  let prev = arr[0];
  for (let i = 1; i < arr.length; i++) {
    const curr = arr[i];
    if (prev > curr) {
      return false;
    }
    prev = curr;
  }
  return true;
}
