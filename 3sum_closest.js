/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    let closestSum = Number.MAX_VALUE;
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            for (let k = j + 1; k < nums.length; k++) {
                if (Math.abs(target - closestSum) > 
                    Math.abs(target - (nums[i] + nums[j] + nums[k])))
                        closestSum = (nums[i] + nums[j] + nums[k]);

            }

        }
    }

    return closestSum;
};
