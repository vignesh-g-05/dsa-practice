/*

        *
      *   *
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *

*/

function bruteForce({ n }) {
  for (let i = 1; i <= 2 * n - 1; i++) {
    for (let j = 1; j <= 2 * n - 1; j++) {
      const total = 2 * n - 1;
      const top = i;
      const left = j;
      const bottom = total - top;
      const right = total - left;
      if (
        top + left === n + 1 ||
        top + right === n ||
        bottom + left === n ||
        left - bottom === n
      ) {
        process.stdout.write("* ");
      } else {
        process.stdout.write("  ");
      }
    }
    console.log();
  }
  console.log();
}

function better({ n }) {
  for (let i = 1; i <= 2 * n - 1; i++) {
    for (let j = 1; j <= 2 * n - 1; j++) {
      const total = 2 * n - 1;
      if (
        i + j === n + 1 ||
        i - j === n - 1 ||
        j - i === n - 1 ||
        i + j === total + n
      ) {
        process.stdout.write("* ");
      } else {
        process.stdout.write("  ");
      }
    }
    console.log();
  }
  console.log();
}
