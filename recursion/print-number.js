let num = 0;

function solution(n) {
  if (num === n) return;
  console.log(++num);
  solution(n);
}
