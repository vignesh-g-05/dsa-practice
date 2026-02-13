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

function pattern20(n) {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < i + 1; j++) {
      process.stdout.write("* ");
    }
    for (let j = 0; j < 2 * n - 2 * (i + 1); j++) {
      process.stdout.write("  ");
    }
    for (let j = 0; j < i + 1; j++) {
      process.stdout.write("* ");
    }
    console.log();
  }
  for (let i = 1; i < n; i++) {
    for (let j = 0; j < n - i; j++) {
      process.stdout.write("* ");
    }
    for (let j = 0; j < 2 * i; j++) {
      process.stdout.write("  ");
    }
    for (let j = 0; j < n - i; j++) {
      process.stdout.write("* ");
    }
    console.log();
  }
}
