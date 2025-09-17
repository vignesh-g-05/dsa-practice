/*

* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *

*/

function pattern1({ n }) {
  for (let i = 0; i < n; i++) {
    let stars = n - i;
    let spaces = 2 * i;
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
  for (let i = n - 1; i > 0; i--) {
    let spaces = (i - 1) * 2;
    let stars = 2 * n - spaces;
    for (let j = 0; j < stars / 2; j++) {
      process.stdout.write("* ");
    }
    for (let j = 0; j < spaces; j++) {
      process.stdout.write("  ");
    }
    for (let j = 0; j < stars / 2; j++) {
      process.stdout.write("* ");
    }
    console.log();
  }
  console.log();
}
