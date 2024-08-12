const asyncTask =  () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('done');
    }, 1000);
  });
}

const foo = async () => {
  const res = await asyncTask();
  console.log(res);
}

console.log('Before Foo Call');
foo();
console.log('After Foo Call');
