/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    const numSet = new Set(nums);
    let smallest = 1;
    while(numSet.has(smallest)) {
        smallest++;
    }
    return smallest;
    
};
