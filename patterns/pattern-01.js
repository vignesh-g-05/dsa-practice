function pattern1(n) {
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < n; col++) {
      process.stdout.write("*");
    }
    console.log();
  }
}
