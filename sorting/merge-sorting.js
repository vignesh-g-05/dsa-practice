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

export function solution3({ arr }) {
  mergeSort(arr, 0, arr.length - 1);
  return arr;
}

function mergeSort(arr, low, high) {
  if (low === high) return;
  const mid = Math.floor((low + high) / 2);
  mergeSort(arr, low, mid);
  mergeSort(arr, mid + 1, high);
  sort(arr, low, mid, high);
}

function sort(arr, low, mid, high) {
  const temp = [];
  let left = low;
  let right = mid + 1;
  while (left <= mid && right <= high) {
    if (arr[left] < arr[right]) {
      temp.push(arr[left]);
      left++;
    } else {
      temp.push(arr[right]);
      right++;
    }
  }
  while (left <= mid) {
    temp.push(arr[left]);
    left++;
  }
  while (right <= high) {
    temp.push(arr[right]);
    right++;
  }
  for (let i = low; i < high; i++) {
    arr[i] = temp[i - low];
  }
}
