/*

A B C D E
A B C D
A B C
A B
A

*/

function pattern11({ n }) {
  for (let i = n; i > 0; i--) {
    let charCode = 65;
    for (let j = 0; j < i; j++) {
      process.stdout.write(String.fromCharCode(charCode++) + " ");
    }
    console.log();
  }
  console.log();
}
