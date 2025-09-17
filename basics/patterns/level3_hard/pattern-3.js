/*

5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5

*/

function myPattern3({ n }) {
  for (let i = 0; i < 2 * n - 1; i++) {
    let changed = false;
    if (i >= n) {
      i = 2 * n - i - 2;
      changed = true;
    }
    for (let j = n; j >= n - i; j--) {
      process.stdout.write(`${j} `);
    }
    for (let j = 0; j < 2 * n - 1 - 2 * (i + 1); j++) {
      process.stdout.write(`${n - i} `);
    }

    for (let j = n - i; j <= n; j++) {
      if (j !== 1) {
        process.stdout.write(`${j} `);
      }
    }

    if (changed) {
      i = 2 * n - 2 - i;
    }

    console.log();
  }
  console.log();
}

function onlinePattern3({ n }) {
  for (let i = 0; i < 2 * n - 1; i++) {
    for (let j = 0; j < 2 * n - 1; j++) {
      const total = 2 * n - 2;
      const top = i;
      const left = j;
      const bottom = total - top;
      const right = total - left;
      process.stdout.write(`${n - Math.min(top, left, bottom, right)} `);
    }
    console.log();
  }
  console.log();
}
