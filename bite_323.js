function intersection(...args) {
  const iterables = args.filter(Boolean).map(iterable => new Set(iterable));
  if (iterables.length > 0) {
    return new Set([...iterables.reduce((a, b) => new Set([...a].filter(x => b.has(x))))]);
  } else {
    return new Set();
  }
}
