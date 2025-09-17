/*

A
B C
D E F
G H I J
K L M N O

*/

function pattern10({ n }) {
  let charCode = 65;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j <= i; j++) {
      process.stdout.write(`${String.fromCharCode(charCode++)} `);
    }
    console.log();
  }
  console.log();
}
