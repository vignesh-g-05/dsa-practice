/*

 *
 * *
 * * *
 * * * *
 * * * * *

 */

function pattern2({ n }) {
  for (let row = 1; row <= n; row++) {
    for (let col = 0; col < row; col++) {
      process.stdout.write("* ");
    }
    console.log();
  }
  console.log();
}
