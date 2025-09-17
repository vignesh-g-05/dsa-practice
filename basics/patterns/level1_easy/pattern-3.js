/*

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5

*/

function pattern3({ n }) {
  for (let row = 1; row <= n; row++) {
    for (let col = 1; col <= row; col++) {
      process.stdout.write(`${col} `);
    }
    console.log();
  }
  console.log();
}
