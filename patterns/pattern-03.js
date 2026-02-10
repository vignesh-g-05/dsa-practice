function pattern3() {
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < row + 1; col++) {
      process.stdout.write(`${col + 1}`);
    }
    console.log();
  }
}
