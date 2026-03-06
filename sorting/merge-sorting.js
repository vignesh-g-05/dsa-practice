function solution1({ arr1, arr2 }) {
  const arr = [];
  let i = 0;
  let j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      arr.push(arr1[i]);
      i++;
    } else {
      arr.push(arr2[j]);
      j++;
    }
  }
  while (i < arr1.length) {
    arr.push(arr1[i]);
    i++;
  }

  while (j < arr2.length) {
    arr.push(arr2[j]);
    j++;
  }

  return arr;
}

export function solution2({ arr }) {
  const result = [];
  const end = arr.length;
  const mid = parseInt(end / 2);

  let i = 0;
  let j = mid + 1;

  while (i <= mid && j < end) {
    if (arr[i] < arr[j]) {
      result.push(arr[i]);
      i++;
    } else {
      result.push(arr[j]);
      j++;
    }
  }

  while (i < mid) {
    result.push(arr[i]);
    i++;
  }

  while (j < end) {
    result.push(arr[j]);
    j++;
  }

  return result;
}
