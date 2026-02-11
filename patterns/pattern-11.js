/*
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
*/

function pattern11(n) {
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < row + 1; col++) {
      process.stdout.write(`${1 - ((row + col) % 2)} `);
    }
    console.log();
  }
}
