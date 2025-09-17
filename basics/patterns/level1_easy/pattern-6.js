/*

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

*/

function pattern6({ n }) {
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < n - row; col++) {
      process.stdout.write(`${col + 1} `);
    }
    console.log();
  }
  console.log();
}
