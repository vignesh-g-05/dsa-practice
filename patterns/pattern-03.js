/*
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
*/

function pattern3() {
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < row + 1; col++) {
      process.stdout.write(`${col + 1}`);
    }
    console.log();
  }
}
