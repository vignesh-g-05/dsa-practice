/*

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

*/

function pattern7({ n }) {
  for (let row = 0; row < n - 1; row++) {
    for (let col = 0; col < row + 1; col++) {
      process.stdout.write("* ");
    }
    console.log();
  }
  for (let col = 0; col < n; col++) {
    process.stdout.write("* ");
  }
  console.log();
  for (let row = n - 1; row > 0; row--) {
    for (let col = 0; col < row; col++) {
      process.stdout.write("* ");
    }
    console.log();
  }
  console.log();
}
