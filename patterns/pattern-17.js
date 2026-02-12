/*
        A
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A
*/
function pattern17(n) {
  for (let i = 0; i < n; i++) {
    let charCode = 65;
    for (let j = 0; j < n - i - 1; j++) {
      process.stdout.write("  ");
    }
    for (let j = 0; j < 2 * i + 1; j++) {
      process.stdout.write(`${String.fromCharCode(charCode)} `);
      if (j < i - 1 / 2) {
        charCode++;
      } else {
        charCode--;
      }
    }
    console.log();
  }
}
