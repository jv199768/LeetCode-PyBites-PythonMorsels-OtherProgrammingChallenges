/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
  var cache = {};
    return function(){
      var key = JSON.stringify(arguments);
      if (cache[key]){
        console.log(cache)
        return cache[key];
      }
      else{
        val = fn.apply(null, arguments);
        cache[key] = val;
        return val; 
      }
  }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
