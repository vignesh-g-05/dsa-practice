/*
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
*/

function pattern22(n) {
  for (let i = 0; i < 2 * n - 1; i++) {
    for (let j = 0; j < 2 * n - 1; j++) {
      const total = 2 * n - 2;
      const top = i;
      const left = j;
      const bottom = total - top;
      const right = total - left;
      const min = Math.min(top, left, bottom, right);
      const num = n - min;
      process.stdout.write(`${num} `);
    }
    console.log();
  }
}
