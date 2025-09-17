/*

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

*/

function pattern3({ n }) {
  for (let row = 0; row < n - 1; row++) {
    for (let space = 0; space < n - row - 1; space++) {
      process.stdout.write("  ");
    }
    for (let star = 0; star < 2 * row + 1; star++) {
      process.stdout.write("* ");
    }
    console.log();
  }
  for (let i = 0; i < 2 * n - 1; i++) {
    process.stdout.write("* ");
  }
  console.log();
  for (let row = 0; row < n - 1; row++) {
    for (let space = 0; space < row + 1; space++) {
      process.stdout.write("  ");
    }
    for (let star = 0; star < 2 * (n - row - 2) + 1; star++) {
      process.stdout.write("* ");
    }
    console.log();
  }
  console.log();
}
