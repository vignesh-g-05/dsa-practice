count = 0;

function solution(n) {
  if (count === n) return n;
  return solve(count++);
}
