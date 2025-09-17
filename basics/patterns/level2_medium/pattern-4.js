/*

1                 1
1 2             2 1
1 2 3         3 2 1
1 2 3 4     4 3 2 1
1 2 3 4 5 5 4 3 2 1

*/

function pattern4({ n }) {
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= i; j++) {
      process.stdout.write(`${j} `);
    }
    for (let k = 1; k <= 2 * n - 2 * i; k++) {
      process.stdout.write("  ");
    }
    for (let l = i; l >= 1; l--) {
      process.stdout.write(`${l} `);
    }
    console.log();
  }
  console.log();
}
