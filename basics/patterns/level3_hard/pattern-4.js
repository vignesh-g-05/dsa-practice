/*

1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
1 2 3 4 5 6 5 4 3 2 1
1 2 3 4 5 6 7 6 5 4 3 2 1

*/

function pattern3({ n }) {
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= 2 * i - 1; j++) {
      const left = j;
      const right = 2 * i - left;
      process.stdout.write(`${Math.min(left, right)} `);
    }
    console.log();
  }
  console.log();
}
