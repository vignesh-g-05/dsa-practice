function solution1(arr1 = [], arr2 = []) {
  if (arr1.length === arr2.length) {
    return arr2;
  }
  arr2.unshift(arr1[arr2.length]);
  return solution1(arr1, arr2);
}

export function solution2(arr1 = [], arr2 = []) {
  if (arr1.length === arr2.length) {
    return arr2;
  }
  arr2.push(arr1[arr1.length - arr2.length - 1]);
  return solution2(arr1, arr2);
}
