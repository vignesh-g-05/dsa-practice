/*

          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *

*/

function pattern1({ n }) {
  for (let row = 0; row < n; row++) {
    for (let space = 0; space < n - row - 1; space++) {
      process.stdout.write("  ");
    }
    for (let star = 0; star < row * 2 + 1; star++) {
      process.stdout.write("* ");
    }
    console.log();
  }
  console.log();
}
