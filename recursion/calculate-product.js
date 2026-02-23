let prod = 1;

function solution(n, i = 1) {
  if (i > n) {
    return prod;
  }

  prod = prod * i;
  return solution(n, i + 1);
}
