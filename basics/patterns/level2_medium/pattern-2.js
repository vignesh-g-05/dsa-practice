/*

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

*/

function pattern2({ n }) {
  for (let row = 0; row < n; row++) {
    for (let space = 0; space < row; space++) {
      process.stdout.write("  ");
    }
    for (let star = 0; star < 2 * (n - row - 1) + 1; star++) {
      process.stdout.write("* ");
    }
    console.log();
  }
  console.log();
}
