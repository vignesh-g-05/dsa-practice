/*
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1
*/

function pattern12(n) {
  for (let row = 1; row < n; row++) {
    for (let col = 1; col < row + 1; col++) {
      process.stdout.write(`${col} `);
    }
    for (let col = 1; col <= 2 * (n - 1) - 2 * row; col++) {
      process.stdout.write(`  `);
    }
    for (let col = row; col > 0 * row; col--) {
      process.stdout.write(`${col} `);
    }
    console.log();
  }
}
