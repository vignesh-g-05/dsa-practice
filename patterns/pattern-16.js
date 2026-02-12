/*
A
B B
C C C
D D D D
E E E E E
*/

function pattern16(n) {
  let charCode = 65;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < i + 1; j++) {
      const char = String.fromCharCode(charCode);
      process.stdout.write(`${char} `);
    }
    charCode++;
    console.log();
  }
}
