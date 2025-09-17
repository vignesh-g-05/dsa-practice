/*

*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *

*/

function pattern2({ n }) {
  for (let i = 1; i < 2 * n; i++) {
    let spaces = i <= n ? 2 * n - 2 * i : 2 * (i - n);
    let stars = (2 * n - spaces) / 2;

    for (let j = 0; j < stars; j++) {
      process.stdout.write("* ");
    }
    for (let j = 0; j < spaces; j++) {
      process.stdout.write("  ");
    }
    for (let j = 0; j < stars; j++) {
      process.stdout.write("* ");
    }
    console.log();
  }
  console.log();
}
