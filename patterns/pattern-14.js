/*
A
A B
A B C
A B C D
A B C D E
*/

function pattern14(n) {
  for (let i = 0; i < n; i++) {
    let charCode = 65;
    for (let j = 0; j < i + 1; j++) {
      const char = String.fromCharCode(charCode++);
      process.stdout.write(`${char} `);
    }
    console.log();
  }
}
