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

function pattern19(n) {
  for (let i = 0; i < n; i++) {
    for (let j = n - i - 1; j >= 0; j--) {
      process.stdout.write(`* `);
    }
    for (let j = 0; j < 2 * i; j++) {
      process.stdout.write("  ");
    }
    for (let j = n - i - 1; j >= 0; j--) {
      process.stdout.write(`* `);
    }
    console.log();
  }
  for (let i = 1; i < n; i++) {
    for (let j = 0; j < i + 1; j++) {
      process.stdout.write("* ");
    }
    for (let j = 2; j < 2 * n - 2 * i; j++) {
      process.stdout.write("  ");
    }
    for (let j = 0; j < i + 1; j++) {
      process.stdout.write("* ");
    }
    console.log();
  }
}
