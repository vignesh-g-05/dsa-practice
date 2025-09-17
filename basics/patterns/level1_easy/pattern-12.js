/*

A
B B
C C C
D D D D
E E E E E

*/

function pattern12({ n }) {
  let charCode = 65;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j <= i; j++) {
      process.stdout.write(String.fromCharCode(charCode) + " ");
    }
    console.log();
    charCode++;
  }
  console.log();
}
