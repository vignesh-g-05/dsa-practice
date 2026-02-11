/*
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
*/

function pattern13(n) {
  let num = 1;
  for (let row = 0; row < n; row++) {
    for (let col = 0; col <= row; col++) {
      process.stdout.write(`${num++} `);
    }
    console.log();
  }
}
