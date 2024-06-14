#include <stdio.h> 

bool isPalindrome(int x) {
    int original_number = x;
    int reversed = 0;
    int num = original_number;
    while (num != 0) {
        int r = num % 10;
        reversed = reversed * 10 + r;
        num /= 10;
    }
    if(original_number==reversed){
        return 1;
    }
    if(x < 0){
        return 0;
    }
    else{
        return 0;
    }
    
}
