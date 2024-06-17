// Fibonacci generator
function* fibonacci() {
  [a, b] = [0, 1]
  while (true) {
    yield a;
    [a, b] = [b, a + b]
  }
}

// Instantiates the fibonacci generator
var fib = fibonacci();

// gets first 10 numbers from the Fibonacci generator starting from 0
for (let i = 0; i < 10; i++) {
  console.log(fib.next().value);
}
