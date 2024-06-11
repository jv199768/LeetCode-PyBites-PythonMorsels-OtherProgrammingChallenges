/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let l = 0, r = -1;
    let sum = 0;
    let minLength = nums.length + 1;
    while (l < nums.length) {
        if(r+1 < nums.length && sum < target){
            sum += nums[++r];
        }
        else {
            sum -= nums[l++];
        }

        if (sum >= target) {
            minLength = Math.min(minLength, r-l+1);
        }
    }
    return minLength == nums.length + 1 ? 0 : minLength;
};
