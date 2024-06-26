#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int bitwiseComplement(int n) {

        int ans = 0;
        if(n==0) return 1;
        for (int i = 0; n > 0; i++) {
            ans += pow(2, i) * (!(n % 2));
            n /= 2;
        }
        return ans;        
    }
};
