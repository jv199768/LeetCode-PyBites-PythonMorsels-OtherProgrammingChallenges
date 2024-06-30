/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    // define output array
    const res = [];
    
    // define dfs, with open and close bracket count, and subarray
    const dfs = (open, close, sub) => {
        // define base case.
        // if open + close equals n x 2, then push to res.
        if (open + close === n*2) {
            res.push(sub.join(''));
            return;
        }
        if (open > close) {
            sub.push(')');
            dfs(open, close+1, sub);
            // backtrack
            sub.pop();
        }
        
        // push open bracket if count < n,
        // and call dfs with incremented open count.
        if (open < n) {
            sub.push('(');
            dfs(open+1, close, sub);
            // backtrack
            sub.pop();
        }
        
        // only push closed bracket if close count < open count,
        // and call dfs with incremented close count.

    }
    
    // call dfs
    dfs(0, 0, []);
    return res;
};
