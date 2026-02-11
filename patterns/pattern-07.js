/*
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
*/

function pattern7() {
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < n - (row + 1); col++) {
      process.stdout.write("  ");
    }
    for (let col = 0; col < 2 * row + 1; col++) {
      process.stdout.write("* ");
    }
    console.log();
  }
}
