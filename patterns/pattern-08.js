/* 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
*/

function pattern8(n) {
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < row; col++) {
      process.stdout.write("  ");
    }
    for (let col = 0; col < 2 * n - 1 - 2 * row; col++) {
      process.stdout.write("* ");
    }
    console.log();
  }
}
