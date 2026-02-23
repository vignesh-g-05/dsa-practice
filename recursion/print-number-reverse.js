function solution(n) {
  if (n === 0) {
    return;
  }
  console.log(n);
  solve(n - 1);
}
