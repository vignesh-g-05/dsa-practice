/*

1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

*/

function pattern8({ n }) {
  for (let i = 1; i <= n; i++) {
    let number = i % 2;
    for (let j = 0; j < i; j++) {
      process.stdout.write(`${number} `);
      number = Number(!number);
    }
    console.log();
  }
  console.log();
}
