const asyncTask =  () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      reject('Something not working!');
    }, 1000);
  });
}

const foo = async () => {
  try {
    const res = await asyncTask();
    console.log(res);
  } catch (err) {
    console.log(err);
  }
  console.log('After calling AsyncTask');
}

foo();
