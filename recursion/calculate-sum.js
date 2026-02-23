let sum = 0;

function solution() {
  if (n === 0) {
    return sum;
  }

  sum = sum + n;
  return solution(n - 1);
}
