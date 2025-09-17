/*

E
D E
C D E
B C D E
A B C D E

*/

function pattern6({ n }) {
  for (let i = 1; i <= n; i++) {
    let charCode = 65 + n - i;
    for (let j = 1; j <= i; j++) {
      process.stdout.write(String.fromCharCode(charCode++) + " ");
    }
    console.log();
  }
  console.log();
}
