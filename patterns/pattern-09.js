/* 
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
*/

export function pattern9(n) {
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < n - row - 1; col++) {
      process.stdout.write("  ");
    }
    for (let col = 0; col < 2 * row + 1; col++) {
      process.stdout.write("* ");
    }
    console.log();
  }
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < row; col++) {
      process.stdout.write("  ");
    }
    for (let col = 0; col < 2 * n - 2 * row - 1; col++) {
      process.stdout.write("* ");
    }
    console.log();
  }
  return null;
}
