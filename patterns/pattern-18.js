/*
E
D E
C D E
B C D E
A B C D E
*/

function pattern18(n) {
  let startCharCode = 64 + n;
  for (let i = 0; i < n; i++) {
    let currCharCode = startCharCode;
    for (let j = 0; j < i + 1; j++) {
      const char = String.fromCharCode(currCharCode++);
      process.stdout.write(`${char} `);
    }
    startCharCode--;
    console.log();
  }
}
