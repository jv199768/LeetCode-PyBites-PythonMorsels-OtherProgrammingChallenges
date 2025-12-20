class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
      
        // Keep removing the rightmost set bit until n becomes 0
        while (n != 0) {
            // n & (n - 1) removes the rightmost set bit
            // Example: n = 1100 (binary), n - 1 = 1011
            // n & (n - 1) = 1100 & 1011 = 1000
            n &= (n - 1);
          
            // Increment count for each set bit removed
            ++count;
        }
      
        return count;
    }
};
