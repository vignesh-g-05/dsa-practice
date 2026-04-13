/*
Time Complexity: O(n)
Space Complexity: O(1)
*/

function solution({ arr }) {
  if (arr.length < 2) {
    return -1;
  }
  if (arr.length === 2 && arr[0] === arr[1]) {
    return arr[0];
  }
  let largest = arr[0];
  let smallest = arr[0];
  let secondLargest = arr[0];
  let secondSmallest = arr[0];

  for (let i = 1; i < arr.length; i++) {
    const curr = arr[i];
    if (curr > largest) {
      secondLargest = largest;
      largest = curr;
    } else if ((curr > secondLargest) & (curr !== largest)) {
      secondLargest = curr;
    } else if (curr < smallest) {
      secondSmallest = smallest;
      smallest = curr;
    } else if (curr < secondSmallest && curr !== smallest) {
      secondSmallest = curr;
    }
  }

  return [secondSmallest, secondLargest];
}
