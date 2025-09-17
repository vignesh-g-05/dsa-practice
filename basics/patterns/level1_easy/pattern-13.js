/*

* * * * *
*       *
*       *
*       *
* * * * *

*/

function pattern13({ n }) {
  for (let i = 0; i < n; i++) {
    if (i === 0 || i === n - 1) {
      for (let i = 0; i < n; i++) {
        process.stdout.write("* ");
      }
    } else {
      process.stdout.write("* ");
      for (let i = 0; i < n - 2; i++) {
        process.stdout.write("  ");
      }
      process.stdout.write("* ");
    }
    console.log();
  }
  console.log();
}
