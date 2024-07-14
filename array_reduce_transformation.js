/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
  let value = init;

  for (const num of nums) {
    value = fn(value, num);
  }

  return value;
};
