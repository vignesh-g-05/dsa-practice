/*

     1
     2 2
     3 3 3
     4 4 4 4
     5 5 5 5 5

*/

function pattern4({ n }) {
  for (let row = 1; row <= n; row++) {
    for (let col = 1; col <= row; col++) {
      process.stdout.write(`${row} `);
    }
    console.log();
  }
  console.log();
}
