function pattern4() {
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < row + 1; col++) {
      process.stdout.write(`${row + 1}`);
    }
    console.log();
  }
}
