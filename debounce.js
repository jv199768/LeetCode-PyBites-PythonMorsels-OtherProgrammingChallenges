/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
  let timeout; // Will store our timer ID

  return function (...args) {
    // Returned function (the debounced version)
    clearTimeout(timeout); // Clear any existing timer

    timeout = setTimeout(() => {
      fn(...args); // Execute original function
    }, t);
  };
}


/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */
