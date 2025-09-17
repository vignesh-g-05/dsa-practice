/*

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

*/
function pattern9({ n }) {
  let number = 1;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j <= i; j++) {
      process.stdout.write(`${number++} `);
    }
    console.log();
  }
  console.log();
}
