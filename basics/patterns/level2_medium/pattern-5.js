/*
      A
    A  B  A
  A  B  C  B  A
A  B  C  D  C  B  A

*/

function pattern5({ n }) {
  for (let i = 1; i < n; i++) {
    let charCode = 65;
    for (let j = 0; j < n - i - 1; j++) {
      process.stdout.write("  ");
    }
    for (let k = n - i; k < n; k++) {
      process.stdout.write(String.fromCharCode(charCode++) + "  ");
    }
    charCode--;
    charCode--;
    while (charCode > 64) {
      process.stdout.write(String.fromCharCode(charCode--) + "  ");
    }
    console.log();
  }
  console.log();
}
