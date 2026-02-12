/*
A B C D E
A B C D
A B C
A B
A
*/

function pattern15(n) {
  for (let i = n; i > 0; i--) {
    let charCode = 65;
    for (let j = 0; j < i; j++) {
      const char = String.fromCharCode(charCode++);
      process.stdout.write(`${char} `);
    }
    console.log();
  }
}
